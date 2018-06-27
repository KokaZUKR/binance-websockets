# -*- coding: utf-8 -*-

base_endpoint = 'wss://stream.binance.com:9443'
ticker = 'bnbbtc'
stream = 'aggTrade'

logfmt = "%(asctime)s:%(levelname)s:binance-websockets:%(name)s:%(filename)s:%(lineno)d:%(message)s"
datefmt = "%Y-%m-%dT%H:%M:%SZ"

database = {
    'connector': '',
    'credentials': {
    }
}

tickers = {
    'bnbbtc',
    'ethbtc'
}

coins = {
    'btc': 'Bitcoin',
    'eth': 'Ethereum',
    'ltc': 'Litecoin',
    'bnb': 'Binance Coin',
}