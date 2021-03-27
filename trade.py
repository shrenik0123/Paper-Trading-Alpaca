from config import *
import requests

headers = {'APCA-API-KEY-ID': API_KEY, 'APCA-API-SECRET-KEY': SECRET_KEY}
BASE_URL = "https://paper-api.alpaca.markets"

ACCOUNT_URL = "{}/v2/account".format(BASE_URL)
r = requests.get(ACCOUNT_URL, headers=headers)
print(r.content)