import os
import requests
from os.path import join, dirname
from dotenv import load_dotenv
import influxdb
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
class InfluxDb(object):

    def __init__(self):
        self._host = os.environ['INFLUX_HOST']
        self._port = os.environ['INFLUX_PORT']
        self._db = os.environ['INFLUX_DB']
        self._read_user =os.environ['INFLUX_READ_USER']
        self._read_passwd = os.environ['INFLUX_READ_PASSWD']
        self._write_user = os.environ['INFLUX_WRITE_USER']
        self._write_passwd = os.environ['INFLUX_WRITE_PASSWD']

    # private methods for internal read client creation
    def _read_client(self):
        return influxdb.InfluxDBClient(self._host, self._port, self._read_user, self._read_passwd)

    # private methods for internal write client creation
    def _write_client(self):
        return InfluxDBClient(self._host, self._port, self._write_user, self._write_passwd, self._db)

    # public method for displaying current influx config
    def get_connection_details(self):
        return {
            "host" : self._host,
            "port" : self._port,
            "db" : self._read_user
        }

    # Generic public query method
    def query(self, query):
        print self._read_client().query(query)

    # Generic public write method
    def write(self):
        return self._write_client().query(query)

if __name__ == '__main__':
    print("Running Influx()")
    client = InfluxDb()

    print client.query("SHOW DATABASES")
