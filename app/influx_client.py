import os
from os.path import join, dirname
from dotenv import load_dotenv
import influxdb
from datetime import datetime, tzinfo
import time
import pytz
import json
# import config # uncomment if using config file vs below import method

# import environment variables - comment out if using config file
APP_ROOT = os.path.join(os.path.dirname(__file__), '..')   # refers to application_top
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)

"""A Python client for connecting, writing and querying to InfluxDB. An InfluxDB
client has the following properties (set these in .env):

Attributes:
    host: address for the influx instance
    port: port that influx is open on
    database: what database the client is to connect to
    user: what user information needs
    password: users password
"""
class InfluxClient(object):

    def __init__(self):
        self._host = os.environ['INFLUX_HOST']
        self._port = os.environ['INFLUX_PORT']
        self._db = os.environ['INFLUX_DB']
        self._read_user =os.environ['INFLUX_READ_USER']
        self._read_passwd = os.environ['INFLUX_READ_PASSWD']
        self._write_user = os.environ['INFLUX_WRITE_USER']
        self._write_passwd = os.environ['INFLUX_WRITE_PASSWD']
        self._read_client = None
        self._write_client = None
        self._logger = open("write_errors.log", "w")

    # private methods for internal read client creation
    def read_client(self):
        if not self._read_client:
            self._read_client = influxdb.InfluxDBClient(self._host, self._port, self._read_user, self._read_passwd, self._db)
        return self._read_client

    # private methods for internal write client creation
    def write_client(self):
        if not self._write_client:
            self._write_client =  influxdb.InfluxDBClient(self._host, self._port, self._write_user, self._write_passwd, self._db)
        return self._write_client

    # Generic public query method
    def query(self, query):
        print self.read_client().query(query)

    # Generic public write method
    def write(self, data):
        return self.write_client().write_points(data)

    # public method for displaying current influx config
    def get_connection_details(self):
        return {
            "host" : self._host,
            "port" : self._port,
            "db" : self._db
        }

    def write_btc_ticker(self,data):
        measurement = "market_data"
        time = data['time']
        tags = dict(coin="BTC", currency="GBP", exchange="GDAX")
        fields = dict(close=float(data['price']))

        data = [dict(measurement=measurement, tags=tags, time=time, fields=fields)]
        self.write(data)

    def write_btc_candles(self,data):
        for candle in data:
            created = candle[0]
            dt = datetime.utcfromtimestamp(created)

            measurement = "market_data"
            time = dt
            tags = dict(coin="BTC", currency="GBP", exchange="GDAX")

            fields = dict(
                low=float(candle[1]),
                high=float(candle[2]),
                open=float(candle[3]),
                close=float(candle[4]),
                volume=float(candle[5])
            )

            data = [dict(measurement=measurement, tags=tags, time=time, fields=fields)]
            self.write(data)

# run the file for a small test!
if __name__ == '__main__':
    print("Running InfluxClient()")

    influx = InfluxClient()
    print influx.get_connection_details()
