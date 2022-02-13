import datetime
from abc import ABC, abstractmethod
from typing import Sequence, Mapping
import requests
import pandas as pd
from dateutil.parser import isoparse
import re
from enum import Enum, auto


def camel_to_snake(name):
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()


class MarketDataAccount(ABC):
    @abstractmethod
    def get_all_current_rates(self, base_asset="USD") -> Mapping[str, float]:
        pass


class CoinMetrics():
    #https://docs.coinmetrics.io/api/v4
    class Decorators():
        @classmethod
        def to_frame(cls, decorated):
            type_map = {'decimal': float, 'bigint': int}

            def wrapper(*arg_list, **arg_dict):
                metrics = arg_list[0].metrics
                df = pd.DataFrame(decorated(*arg_list, **arg_dict)).fillna(0)
                df.columns = [camel_to_snake(col) for col in df.columns]
                if "time" in df.columns:
                    df.time = df.time.apply(isoparse)
                for col in [c for c in df.columns if c in metrics]:
                    df[col] = df[col].apply(type_map[metrics[col]["data_type"]])
                for col in  [c for c in df.columns if "price" in c]:
                    df[col] = df[col].apply(float)
                for col in  [c for c in df.columns if "volume" in c]:
                    df[col] = df[col].apply(float)
                return df

            return wrapper

    class MarketType(Enum):
        spot = auto()
        future = auto()
        option = auto()

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.coinmetrics.io/v4"
        self.metrics = self.catalog_metrics()

    @Decorators.to_frame
    def market_candles(self, markets: Sequence[str], frequency: str = '1d',
                      start_time: str = None, end_time: str = None) -> Sequence[Mapping]:
        return self.api_call(end_point="/timeseries/market-candles", markets=markets, frequency=frequency,
                             start_time=start_time, end_time=end_time, paging_from="start", page_size=10000)

    @Decorators.to_frame
    def asset_metrics(self, assets: Sequence[str], metrics: Sequence[str], frequency: str = '1d',
                      start_time: str = None, end_time: str = None) -> Sequence[Mapping]:
        return self.api_call(end_point="/timeseries/asset-metrics", assets=assets, metrics=metrics, frequency=frequency,
                             start_time=start_time, end_time=end_time, paging_from="start", page_size=10000)

    @Decorators.to_frame
    def market_funding_rates(self, markets: Sequence[str], start_time: str = None, end_time: str = None):
        return self.api_call(end_point="/timeseries/market-funding-rates", markets=markets, start_time=start_time,
                             end_time=end_time)

    def catalog_metrics(self, metrics: Sequence[str] = []):
        out = self.api_call(end_point="/catalog/metrics", metrics=metrics)
        return {camel_to_snake(metric["metric"]): metric for metric in out}

    def catalog_markets(self, markets: Sequence[str] = None, exchange: Sequence[str] = None,
                        type: MarketType = None, base: str = None, quote: str = None, asset: str = None,
                        symbol: str = None):
        out = self.api_call(end_point="/catalog-all/markets", markets=markets, exchange=exchange, type=type.name if type is not None else None,
                            base=base, quote=quote, asset=asset, symbol=symbol)
        return {market["market"]: market for market in out}

    def catalog_assets(self, assets: Sequence[str] = None):
        out = self.api_call(end_point="/catalog-all/assets", assets=assets)
        return {asset["asset"].upper(): asset for asset in out}

    def api_call(self, end_point, **argd) -> Sequence[Mapping]:
        data = []

        def normalize_val(val):
            if type(val) == list:
                return ",".join(val)
            else:
                return str(val)

        params = {k: normalize_val(v) for k, v in argd.items() if v}
        params["api_key"] = self.api_key
        param_list = [f'{k}={v}' for k, v in params.items()]
        url = f'{self.base_url}{end_point}?{"&".join(param_list)}'
        response = requests.get(url=url)
        if response.status_code == 200:
            data += response.json()["data"]
            while "next_page_url" in response.json():
                response = requests.get(url=response.json()["next_page_url"])
                if response.status_code == 200:
                    data += response.json()["data"]
                else:
                    raise ConnectionError(f"{response.json()['type']}: {response.json()['message']}")
            return data
        else:
            raise AttributeError(f"{response.json()['error']['type']}: {response.json()['error']['message']}")
