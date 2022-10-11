import utils.kaiko as k
import os
import datetime as dt


def main():
    kaiko_key = os.getenv("KAIKO_KEY")
    print(kaiko_key)
    kaiko = k.Kaiko(kaiko_key)

    test1 = kaiko.candles(exchange="bfnx", instrument_class="spot", instrument="btc-usd", start_time=dt.datetime(2020, 7, 1, 0, 0, 0).isoformat() + "Z",
                              end_time=dt.datetime(2022, 8, 1, 0, 0, 0).isoformat() + "Z")


    print(test1)





    print("the end")

if __name__ == "__main__":
    main()
