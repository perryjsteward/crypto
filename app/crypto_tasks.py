
from influx_client import InfluxClient
from gdax_client import GdaxClient

# from apscheduler.schedulers.blocking import BlockingScheduler
# sched = BlockingScheduler() # Use blocking for testing

from apscheduler.schedulers.background import BackgroundScheduler
sched = BackgroundScheduler() # Use background for prod

influx = InfluxClient()
gdax = GdaxClient()

"""
A Python script for managing scheduled tasks for the cryto tracking application
"""

# @sched.scheduled_job('interval', id='update_btc_candles', hours=2)
def update_btc_candles():
    data = gdax.get_btc_candles()
    influx.write_btc_candles(data)


# @sched.scheduled_job('interval', id='update_btc_ticker', minutes=1)
# def update_btc_ticker():
#     data = gdax.get_btc_ticker()
#     influx.write_btc_ticker(data)

sched.start()
