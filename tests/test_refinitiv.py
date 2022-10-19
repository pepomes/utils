from datetime import date, timedelta
import argparse
import os
from utils.refinitiv.datascope import (
    QuotaContext,
    CredentialedHTTP,
    RefinitivCredentialsProvider,
    HTTP,
    ExtractionsContext,
    DateRange,
    eod_request,
    intraday_bars_request,
    dump_response,
    SearchRequest,
    CsvWriter
)
from utils.refinitiv.enums import EndOfDayField, QuotaCategoryCode, InstrumentTypeGroup, IdentifierType, IntradayField, SummaryInterval
from utils.refinitiv.rics import HRP_UNIVERSE


def dump_quota_info(http: HTTP):
    context = QuotaContext(http)
    for qi in context.get_quota_info():
        print(qi)
    for code in QuotaCategoryCode:
        for ric in context.get_authorized_ric_list(code):
            print(ric)

def main2():
    dss_pass = os.getenv("DSS_PASS")
    dss_login = os.getenv("DSS_LOGIN")
    today = date.today()
    last_date = today - timedelta(days=1)
    first_date = today - timedelta(days=2)
    destination_uri = "./hist_data.csv"

    http = CredentialedHTTP(RefinitivCredentialsProvider(dss_login, dss_pass, HTTP()))

    fields = [
        IntradayField.CloseAsk,
        IntradayField.CloseBid,
        IntradayField.Last,
        IntradayField.Volume
    ]

    rics = ["0#AD:"]

    request = intraday_bars_request(rics,
                                              fields,
                                              DateRange(first_date, last_date),
                                              SummaryInterval.ONE_HOUR,
                                              IdentifierType.ChainRic)

    writer = CsvWriter(destination_uri)
    ExtractionsContext(http).extract_raw(request, writer)


def main(destination_uri, rics, first_date, last_date):

    dss_pass = os.getenv("DSS_PASS")
    dss_login = os.getenv("DSS_LOGIN")
    http = CredentialedHTTP(RefinitivCredentialsProvider(dss_login, dss_pass, HTTP()))

    fields = [
        EndOfDayField.AssetTypeDescription,
        EndOfDayField.AssetSubTypeDescription,
        EndOfDayField.InstrumentID,
        EndOfDayField.TradeDate,
        EndOfDayField.UniversalClosePrice,
        EndOfDayField.InverseRateMarker,
        EndOfDayField.CurrencyCode,
        EndOfDayField.Volume,
    ]

    request = eod_request(rics, fields, DateRange(first_date, last_date), IdentifierType.ChainRic)
    instr_type_groups = \
        [
            InstrumentTypeGroup.Money,
            InstrumentTypeGroup.Commodities,
            InstrumentTypeGroup.Equities,
            InstrumentTypeGroup.FuturesAndOptions
        ]
    #request = SearchRequest(instr_type_groups)
    writer = CsvWriter(destination_uri)
    ExtractionsContext(http).extract_raw(request, writer)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Request Elektron data from refinitiv.")
    parser.add_argument("output", type=str, help="The destination URI to write data to (e.g., s3://bucket/key.csv.gz)")
    # parser.add_argument("first-date", dest="first_date", type=str, help="The first date to fetch (default: today - 1d - 30y)", required=False)
    # parser.add_argument("last-date", dest="last_date", type=str, help="The last date to fetch (default: today - 1d)", required=False)
    today_str = date.today().strftime("%Y-%m-%d")
    args = parser.parse_args([f"/Users/pepomes/Downloads/refinitiv_test_{today_str}.csv"])

    today = date.today()
    last_date = today - timedelta(days=1)
    first_date = last_date.replace(year=today.year - 1)

    #main(args.output, ["0#AD:"], first_date, last_date)
    main2()
