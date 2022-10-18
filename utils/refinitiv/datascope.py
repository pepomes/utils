import datetime
import functools
import json
import time
from dataclasses import dataclass
from http import HTTPStatus
from typing import Dict, List, Iterable
import pandas as pd

import requests

from utils.refinitiv.enums import (
    RefinitivField,
    EndOfDayField,
    TimeAndSalesField,
    IntradayField,
    SummaryInterval,
    TemplateType,
    RequestType,
    SearchType,
    QuotaCategoryCode,
    AssetClass,
    InstrumentTypeGroup,
    IdentifierType
)


def reuters_url(endpoint: str) -> str:
    return "https://selectapi.datascope.refinitiv.com/RestApi/v1/" + endpoint


@dataclass(frozen=True)
class DateRange:
    first: datetime.date
    last: datetime.date


@dataclass(frozen=True)
class Credentials:
    user_name: str
    token: str

    def headers(self, additional_headers: Dict = None):
        headers = {
            "Authorization": f"Token {self.token}",
            "Prefer": "odata.maxpagesize=100000; respond-async;",
            "Content-Type": "application/json; odata=minimalmetadata",
        }
        if additional_headers is not None:
            headers.update(additional_headers)

        return headers


class HTTP:
    def post(self, url, json, headers: Dict = None, **kwargs) -> requests.Response:
        return requests.post(url, json=json, headers=headers, **kwargs)

    def get(self, url, headers: Dict = None, **kwargs) -> requests.Response:
        return requests.get(url, headers=headers, **kwargs)


def cache(f):
    f.__cached_value__ = None

    @functools.wraps(f)
    def wrapped(*args, force_refresh=False, **kwargs):
        if f.__cached_value__ is None or force_refresh:
            f.__cached_value__ = f(*args, **kwargs)
        return f.__cached_value__

    return wrapped


class RefinitivCredentialsProvider:
    def __init__(self, user_name, password, requests: HTTP):
        self.user_name = user_name
        self.password = password
        self._requests = requests

    @cache
    def get_credentials(self) -> Credentials:
        data = {"Credentials": {"Username": self.user_name, "Password": self.password}}

        url = reuters_url("Authentication/RequestToken")
        response = self._requests.post(url, json=data)
        if response.status_code == HTTPStatus.OK:
            token = as_dict(response)["value"]
            return Credentials(self.user_name, token)
        else:
            response.raise_for_status()


@dataclass
class CredentialedHTTP(HTTP):
    credentials_provider: RefinitivCredentialsProvider

    def post(self, url: str, json: Dict = None, headers: Dict = None, **kwargs) -> requests.Response:
        credentials = self.credentials_provider.get_credentials()
        response = requests.post(url, json=json, headers=credentials.headers(headers), **kwargs)

        if response.status_code == HTTPStatus.UNAUTHORIZED:
            credentials = self.credentials_provider.get_credentials(force_refresh=True)
            response = requests.post(url, json=json, headers=credentials.headers(headers), **kwargs)

        return response

    def get(self, url: str, headers: Dict = None, **kwargs) -> requests.Response:
        credentials = self.credentials_provider.get_credentials()
        response = requests.get(url, headers=credentials.headers(headers), **kwargs)

        if response.status_code == HTTPStatus.UNAUTHORIZED:
            credentials = self.credentials_provider.get_credentials(force_refresh=True)
            response = requests.get(url, headers=credentials.headers(headers), **kwargs)

        return response


class UsersContext:
    def __init__(self, requests: HTTP):
        self._requests = requests

    def get_user(self, user_name: str) -> Dict:
        response = self._requests.get(reuters_url(f"Users/Users({user_name})"))
        return as_dict(response)


@dataclass(frozen=True)
class ExtractionRequest:
    request_type: RequestType
    rics: Iterable[str]
    fields: Iterable[RefinitivField]
    condition: Dict
    identifier_type: IdentifierType

    def to_dict(self):
        return {
            "ExtractionRequest": {
                "@odata.type": f"#DataScope.Select.Api.Extractions.ExtractionRequests.{self.request_type.value}",
                "ContentFieldNames": [f.value for f in self.fields],
                "IdentifierList": {
                    "@odata.type": "#DataScope.Select.Api.Extractions.ExtractionRequests.InstrumentIdentifierList",
                    "InstrumentIdentifiers": [{"Identifier": ric, "IdentifierType": self.identifier_type.value} for ric in self.rics],
                    "UseUserPreferencesForValidationOptions": "false",
                },
                "Condition": self.condition,
            }
        }


@dataclass(frozen=True)
class SearchRequest:
    instrument_type_groups: Iterable[InstrumentTypeGroup]

    def to_dict(self):
        return {
            "SearchRequest": {
                "@odata.context": "http://selectapi.datascope.refinitiv.com:83/RestApi.Help/$metadata#DataScope.Select.Api.Search.AllInstrumentSearchRequest",
                "InstrumentTypeGroups": [instr_type_group.name for instr_type_group in self.instrument_type_groups],
                "Identifier": "*",
                "IdentifierType": "Ric",
                "PreferredIdentifierType": "Ric"
            }
        }


class Writer:
    def write(self, filestream):
        raise NotImplementedError


class CsvWriter(Writer):
    def __init__(self, location: str):
        self.location = location

    def write(self, filestream):
        with open(self.location, 'w') as f:
            f.write(filestream.text)


def intraday_bars_request(rics: Iterable[str], fields: Iterable[IntradayField], date_range: DateRange,
                          interval: SummaryInterval, identifier_type: IdentifierType) -> ExtractionRequest:
    condition = {
        "MessageTimeStampIn": "GmtUtc",
        "ReportDateRangeType": "Range",
        "QueryStartDate": date_range.first.strftime("%Y-%m-%d"),
        "QueryEndDate": date_range.last.strftime("%Y-%m-%d"),
        "SummaryInterval": interval.value,
        "TimebarPersistence": "true",
        "DisplaySourceRIC": "true",
    }
    return ExtractionRequest(RequestType.INTRADAY_BARS, rics, fields, condition=condition, identifier_type=identifier_type)


def eod_request(rics: Iterable[str], fields: Iterable[EndOfDayField], date_range: DateRange, identifier_type: IdentifierType) -> ExtractionRequest:
    condition = {
        "ReportDateRangeType": "Range",
        "QueryStartDate": date_range.first.strftime("%Y-%m-%d"),
        "QueryEndDate": date_range.last.strftime("%Y-%m-%d"),
    }
    return ExtractionRequest(RequestType.END_OF_DAY, rics, fields, condition, identifier_type=identifier_type)


def time_and_sales_request(rics: Iterable[str], fields: Iterable[TimeAndSalesField], date_range: DateRange, identifier_typeIdentifierType) -> ExtractionRequest:
    condition = {
        "ReportDateRangeType": "Range",
        "QueryStartDate": date_range.first.strftime("%Y-%m-%d"),
        "QueryEndDate": date_range.last.strftime("%Y-%m-%d"),
    }
    return ExtractionRequest(RequestType.TIME_AND_SALES, rics, fields, condition, identifier_type=identifier_type)


class ExtractionsContext:
    def __init__(self, requests: HTTP):
        self._requests = requests

    def meta_data(self) -> requests.Response:
        endpoint = "Extractions/$metadata"
        response = self._requests.get(reuters_url(endpoint))
        return response

    def get_valid_fields(self, template_type: TemplateType) -> List[str]:
        endpoint = f"Extractions/GetValidContentFieldTypes(ReportTemplateType=DataScope.Select.Api.Extractions.ReportTemplates.ReportTemplateTypes'{template_type.value}')"
        response = self._requests.get(reuters_url(endpoint))
        content = as_dict(response)["value"]
        return [c["Name"] for c in content]

    def extract_raw(self, request: ExtractionRequest, writer: Writer) -> None:
        url = reuters_url("Extractions/ExtractRaw")
        response = self._requests.post(url, request.to_dict())

        dump_response(response)

        if response.status_code == 202:
            request_url = response.headers["location"]

            while response.status_code == 202:
                date_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"{date_str}: Waiting for data from {request_url}...")
                time.sleep(30)
                response = self._requests.get(request_url)

        if response.status_code != 200:
            raise RuntimeError(response)

        dump_response(response)
        # notes = as_dict(response)["Notes"]
        job_id = as_dict(response)["JobId"]
        request_headers = {"Content-Type": "text/plain", "Accept-Encoding": "gzip", "X-Direct-Download": "True"}
        url = reuters_url(f"Extractions/RawExtractionResults('{job_id}')/$value")

        r5 = self._requests.get(url, headers=request_headers, stream=True)
        # Ensure we do not automatically decompress the data on the fly:
        r5.raw.decode_content = False
        writer.write(filestream=r5)

    def search(self, request: SearchRequest, write_loc: str) -> None:
        search_res = pd.DataFrame()
        url = reuters_url("Search/InstrumentSearch")
        print(request.to_dict())
        response = self._requests.post(url, request.to_dict())

        search_res = search_res.append(pd.DataFrame(response.json()["value"]))

        while "@odata.nextlink" in response.json():
            response = self._requests.post(response.json()["@odata.nextlink"], request.to_dict())
            search_res = search_res.append(pd.DataFrame(response.json()["value"]))

        if response.status_code != 200:
            raise RuntimeError(response)

        search_res.to_csv(write_loc)




@dataclass(frozen=True)
class QuotaDetails:
    count: int
    limit: int
    category_code: QuotaCategoryCode
    category_name: str


@dataclass(frozen=True)
class AuthorizedRIC:
    asset_class: AssetClass
    ric: str
    authorization_date: datetime.date
    authorization_description: str
    authorization_user_id: str


@dataclass(frozen=True)
class QuotaContext:
    _requests: HTTP

    def get_quota_info(self) -> List[QuotaDetails]:
        url = reuters_url("Quota/GetQuotaInformation")
        response = self._requests.get(url)
        values = as_dict(response)["value"]
        ret = []
        for v in values:
            qd = QuotaDetails(v["Count"], v["Limit"], QuotaCategoryCode(v["Category"]["Code"]), v["Category"]["Name"])
            ret.append(qd)
        return ret

    def get_authorized_ric_list(self, category_code: QuotaCategoryCode) -> List[AuthorizedRIC]:
        url = reuters_url(f"Quota/GetAuthorizedRicList(CategoryCode='{category_code.value}')")
        response = self._requests.get(url)
        values = as_dict(response)["value"]
        ret = []
        for v in values:
            ric = AuthorizedRIC(AssetClass(v["AssetClass"]), v["AuthorizedValue"], v["AuthorizationDate"], v["AuthorizationDescription"],
                                v["AuthorizationUserId"], )
            ret.append(ric)
        return ret


def as_dict(response: requests.Response) -> Dict:
    if len(response.text) == 0:
        return {}
    return json.loads(response.text)


def dump_response(response: requests.Response) -> None:
    print(f" Response ({response.status_code}) ".center(80, "="))
    try:
        to_print = json.dumps(as_dict(response), indent=2).replace(r"\n", "\n")
    except json.JSONDecodeError:
        to_print = response.text
    print(f"Content: {to_print}")
    print(f" End Response ".center(80, "-"))
