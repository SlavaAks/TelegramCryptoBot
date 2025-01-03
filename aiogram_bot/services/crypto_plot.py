import base64
import io
import os

import ccxt
# import mplfinance as mpf
import pandas as pd
import matplotlib.pyplot as plt

from datetime import datetime

from aiogram.types import BufferedInputFile

from services.historical_market_data import scrape_ohlcv


def plot_ticker(exchange_id, max_retries, symbol, timeframe, since, limit):
    exchange = getattr(ccxt, exchange_id)({
        'enableRateLimit': True,  # required by the Manual
    })
    # convert since from string to milliseconds integer if needed
    if isinstance(since, str):
        since = exchange.parse8601(since)
    # preload all markets from the exchange
    exchange.load_markets()
    ticker_data = scrape_ohlcv(exchange, max_retries, symbol, timeframe, since, limit)

    df = pd.DataFrame(ticker_data)

    df.columns = ["Date", "Open", "High", "Low", "Close", "Volume"]
    print(df)
    # df = pd.read_csv("\\data\\raw\\Binance\\btc_usdt_15m.csv")
    # datetime.utcfromtimestamp(int(df.index)/1000).strftime('%Y-%m-%d %H:%M:%S')

    df["Date"] = [datetime.fromtimestamp(x / 1000.0) for x in df["Date"]]
    df = df.set_index("Date")
    print(df)

    fig, axes = plt.subplots()
    axes.plot(df.index, df["Close"])

    os.remove(".\\plot.png")
    fig.savefig("plot.png")


    # mpf.plot(df, type='candle', mav=(3, 6, 9), volume=True)


if __name__ == '__main__':
    plot_ticker('okx', 3, 'LINK/USDT', '15m', '2024-12-3100:00:00Z', 1000)
