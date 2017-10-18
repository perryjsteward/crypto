import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

INFLUX_HOST = os.environ['INFLUX_HOST']
INFLUX_PORT = os.environ['INFLUX_PORT']
INFLUX_DB = os.environ['INFLUX_DB']
INFLUX_READ_USER = os.environ['INFLUX_READ_USER']
INFLUX_READ_PASSWD = os.environ['INFLUX_READ_PASSWD']
INFLUX_WRITE_USER = os.environ['INFLUX_WRITE_USER']
INFLUX_WRITE_PASSWD = os.environ['INFLUX_WRITE_PASSWD']
