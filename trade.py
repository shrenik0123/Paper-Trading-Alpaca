from requests.api import request
from config import *
import requests
import json

headers = {'APCA-API-KEY-ID': API_KEY, 'APCA-API-SECRET-KEY': SECRET_KEY}

# Necessary URLs
BASE_URL = "https://paper-api.alpaca.markets"
ACCOUNT_URL = "{}/v2/account".format(BASE_URL)
ORDERS_URL = "{}/v2/orders".format(BASE_URL)
WATCHLIST_URL = "{}/v2/watchlists".format(BASE_URL)

def get_account():
    r = requests.get(ACCOUNT_URL, headers=headers)
    return json.loads(r.text)

def get_orders():
    r = requests.get(ORDERS_URL, headers=headers)
    return json.loads(r.text)

def post_order(symbol, qty, side, type, time_in_force):
    data = {
        "symbol": symbol,
        "qty": qty,
        "side": side,
        "type": type,
        "time_in_force": time_in_force
    }
    r = requests.post(ORDERS_URL, data=json.dumps(data), headers=headers)
    return json.loads(r.text)

def get_watchlist():
    r = requests.get(WATCHLIST_URL, headers=headers)
    return json.loads(r.text)

def post_watchlist(watchlist_name, symbols):
    data = {
        "name": watchlist_name,
        "symbols": symbols
    }
    r = requests.post(WATCHLIST_URL, data=json.dumps(data), headers=headers)
    return json.loads(r.text)

# Order 10 apple shares
# response = post_order("AAPL", 10, "buy", "market", "gtc")
# print(json.dumps(response, indent=3))

stocks_to_watch = ["AAPL", "MSFT", "XOM", "PFE"]
response = post_watchlist("First Watchlist", stocks_to_watch)
print(json.dumps(response, indent=3))

response = get_watchlist()
print(json.dumps(response, indent=3))

