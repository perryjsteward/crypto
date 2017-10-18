import config
import influxdb
from influxdb.client import InfluxDBClientError

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
        self._host = config.INFLUX_HOST
        self._port = config.INFLUX_PORT
        self._db = config.INFLUX_DB
        self._read_user = config.INFLUX_READ_USER
        self._read_passwd = config.INFLUX_READ_PASSWD
        self._write_user = config.INFLUX_WRITE_USER
        self._write_passwd = config.INFLUX_WRITE_PASSWD

if __name__ == '__main__':
    print("Running Influx()")
