import ccxt


def get_crypto_price(symbol: str, exchange_id: str) -> str:
    exchange = getattr(ccxt, exchange_id)
    ticker = symbol.upper() + '/USDT'
    price = exchange().fetch_ticker(ticker)['last']
    return price
