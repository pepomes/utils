from datetime import date, timedelta
import argparse

from utils.refinitiv.datascope import (
    QuotaContext,
    CredentialedHTTP,
    RefinitivCredentialsProvider,
    HTTP,
    ExtractionsContext,
    DateRange,
    eod_request,
    dump_response,
    SearchRequest,
    CsvWriter
)
from utils.refinitiv.enums import EndOfDayField, QuotaCategoryCode, InstrumentTypeGroup
from utils.refinitiv.rics import HRP_UNIVERSE


def dump_quota_info(http: HTTP):
    context = QuotaContext(http)
    for qi in context.get_quota_info():
        print(qi)
    for code in QuotaCategoryCode:
        for ric in context.get_authorized_ric_list(code):
            print(ric)


def main(destination_uri, rics, first_date, last_date):

    http = CredentialedHTTP(RefinitivCredentialsProvider("9023248", "uKyJMzyMj@6RrVGarktT", HTTP()))

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

    #request = eod_request(rics, fields, DateRange(first_date, last_date))
    instr_type_groups = \
        [
            InstrumentTypeGroup.Money,
            InstrumentTypeGroup.Commodities,
            InstrumentTypeGroup.Equities,
            InstrumentTypeGroup.FuturesAndOptions
        ]
    request = SearchRequest(instr_type_groups)
    writer = CsvWriter(destination_uri)
    ExtractionsContext(http).search(request, "/Users/pepomes/Downloads/money_ric.csv")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Request Elektron data from refinitiv.")
    parser.add_argument("output", type=str, help="The destination URI to write data to (e.g., s3://bucket/key.csv.gz)")
    # parser.add_argument("first-date", dest="first_date", type=str, help="The first date to fetch (default: today - 1d - 30y)", required=False)
    # parser.add_argument("last-date", dest="last_date", type=str, help="The last date to fetch (default: today - 1d)", required=False)
    today_str = date.today().strftime("%Y-%m-%d")
    args = parser.parse_args([f"/Users/pepomes/Downloads/refinitiv_{today_str}.csv"])

    today = date.today()
    last_date = today - timedelta(days=1)
    first_date = last_date.replace(year=today.year - 1)

    main(args.output, ["EUR="], first_date, last_date)
