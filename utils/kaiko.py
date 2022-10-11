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


class Kaiko():
    # https://docs.coinmetrics.io/api/v4

    class Decorators():
        @classmethod
        def to_frame(cls, transpose=False):
            type_map = {'decimal': float, 'bigint': int}

            def outter(decorated, *arg_list, **arg_dict):
                def wrapper(*arg_list, **arg_dict):
                    #metrics = arg_list[0].metrics
                    metrics = {}
                    df = pd.DataFrame(decorated(*arg_list, **arg_dict)).fillna(0)
                    if transpose: df = df.transpose()
                    df.columns = [camel_to_snake(col) for col in df.columns]
                    if "time" in df.columns:
                        df.time = df.time.apply(isoparse)
                    for col in [c for c in df.columns if c in metrics]:
                        df[col] = df[col].apply(type_map[metrics[col]["data_type"]])
                    for col in [c for c in df.columns if "price" in c]:
                        df[col] = df[col].apply(float)
                    for col in [c for c in df.columns if "volume" in c]:
                        df[col] = df[col].apply(float)
                    return df

                return wrapper

            return outter

    class MarketType(Enum):
        spot = auto()
        future = auto()
        option = auto()

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://eu.market-api.kaiko.io/v2/data"

    @Decorators.to_frame()
    def asset_price(self, base_asset: str, quote_asset: str, interval: str = '1d',
                      start_time: str = None, end_time: str = None):
        return self.api_call(end_point=f"/trades.v1/spot_direct_exchange_rate/{base_asset}/{quote_asset}", interval=interval,
                             start_time=start_time, end_time=end_time)

    @Decorators.to_frame()
    def candles(self, exchange: str, instrument_class: str, instrument: str, interval: str = '1d',
                      start_time: str = None, end_time: str = None):
        return self.api_call(end_point=f"/trades.v1/exchanges/{exchange}/{instrument_class}/{instrument}/aggregations/ohlcv", interval=interval,
                             start_time=start_time, end_time=end_time)


    def api_call(self, end_point, **argd) -> Sequence[Mapping]:
        data = []

        def normalize_val(val):
            if type(val) == list:
                return ",".join(val)
            else:
                return str(val)
        headers = {
            "X-Api-Key": self.api_key,
            "Accept": "application/json",
            "Accept-Encoding": "gzip",
        }
        params = {k: normalize_val(v) for k, v in argd.items() if v}
        param_list = [f'{k}={v}' for k, v in params.items()]
        url = f'{self.base_url}{end_point}?{"&".join(param_list)}'
        print(url)
        response = requests.get(url=url, headers=headers)
        print(response.json())
        if response.status_code == 200:
            data += response.json()["data"]
            while "next_url" in response.json():
                response = requests.get(url=response.json()["next_url"], headers=headers)
                print(response.json())
                if response.status_code == 200:
                    data += response.json()["data"]
                else:
                    raise ConnectionError(f"{response.json()['type']}: {response.json()['message']}")
            return data
        else:
            print(response.json())
            raise AttributeError(f"{response.json()['error']['type']}: {response.json()['error']['message']}")
