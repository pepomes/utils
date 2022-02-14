import utils.coinmetrics as cm
import os



def main():
    cm_key = os.getenv("CM_KEY")
    print(cm_key)
    coinmetrics = cm.CoinMetrics(cm_key)

    test1 = coinmetrics.market_candles(["binance-DOTUSD_210625-future", "huobi-EOS210625_CQ-future"])

    test2 = coinmetrics.catalog_markets()
    print(test2)





    print("the end")

if __name__ == "__main__":
    main()
