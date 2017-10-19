
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

@sched.scheduled_job('interval', id='my_job_id', seconds=5)
def update_btc_candles():
    try:
        data = gdax.get_btc_candles()
        influx.write_coin_candles(data)
    except:
        print "Error updating Bitcoin candles"


@sched.scheduled_job('interval', id='my_job_id', seconds=2)
def update_btc_ticker():
    try:
        data = gdax.get_btc_ticker()
        influx.write_coin_ticker(data)
    except:
        print "Error updating Bitcoin ticker"

sched.start()
