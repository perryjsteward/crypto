import os
import requests
import json
from os.path import join, dirname
from dotenv import load_dotenv
# import config # uncomment if using config file vs below import method

# import environment variables - comment out if using config file
APP_ROOT = os.path.join(os.path.dirname(__file__), '..')   # refers to application_top
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)

"""A Python client for querying GDAX API. Provides historical and current data
for Bitcoin, LiteCoin and Ethereum.

returns costs in GBP.

Attributes:
    api_base: base path for api
"""

class GdaxClient(object):

    def __init__(self):
        self._api_base = os.environ["GDAX_API_BASE"];

    # Return connection obbject data for the client
    def get_connection_details(self):
        return {
            "api_base" : self._api_base
        }

    # Return list of available products in the GDAX exchange
    def get_products(self):
        url = "{}/products".format(self._api_base)
        r = requests.get(url=url)
        return r.json()

    def get_btc_ticker(self):
        url = "{}/products/BTC-GBP/ticker".format(self._api_base)
        r = requests.get(url=url)
        return r.json()

    # Returns historical data for Bitcoin - default is 200 data points, 1 per minute
    def get_btc_candles(self):
        url = "{}/products/BTC-GBP/candles".format(self._api_base)
        r = requests.get(url=url)
        return r.json()

# run the file for a small test!
if __name__ == '__main__':
    print("Running GdaxClient()")
    gdax = GdaxClient()
    print gdax.get_btc_ticker()
