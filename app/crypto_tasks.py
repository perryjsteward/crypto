
from influx_client import InfluxClient
from gdax_client import GdaxClient
import datetime as dt

# from apscheduler.schedulers.blocking import BlockingScheduler
# sched = BlockingScheduler() # Use blocking for testing

from apscheduler.schedulers.background import BackgroundScheduler
sched = BackgroundScheduler() # Use background for prod

influx = InfluxClient()
gdax = GdaxClient()


"""
A Python script for managing scheduled tasks for the cryto tracking application
"""
# update past 3 hours with 1 minute price ticks
@sched.scheduled_job('interval', id='hourly_btc_candle_update', hours=1)
def hourly_btc_candle_update():
    tracker_type = 'ticker'
    data = gdax.get_btc_candles()
    influx.write_btc_candles(data, tracker_type)

# updates hourly candles for the last week
@sched.scheduled_job('interval', id='daily_btc_candle_update', days=1)
def daily_btc_candle_update():
    granularity = 1 * 60 * 60 # 1 hour
    time_delta = dt.timedelta(days=1) # a day ago
    start = dt.datetime.utcnow() - time_delta
    end = dt.datetime.utcnow()
    tracker_type = 'candle'

    params = dict(start=start, end=end, granularity=granularity)
    data = gdax.get_btc_candles(params)
    influx.write_btc_candles(data, tracker_type)

#@sched.scheduled_job('interval', id='update_btc_ticker', minutes=1)
#def update_btc_ticker():
#    data = gdax.get_btc_ticker()
#    influx.write_btc_ticker(data)

sched.start()
