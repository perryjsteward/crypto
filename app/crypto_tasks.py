
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
# @sched.scheduled_job('interval', id='hourly_btc_candle_update', hours=1)
# def hourly_btc_candle_update():
#     granularity = 1 * 60 # 1 minute
#     time_delta = dt.timedelta(hours=2) # 2 hours ago
#     start = dt.datetime.utcnow() - time_delta
#     end = dt.datetime.utcnow()
#
#     params = dict(start=start, end=end, granularity=granularity)
#     data = gdax.get_btc_candles(params)
#     influx.write_btc_candles(data)

# updates hourly candles for the last day
@sched.scheduled_job('interval', id='daily_btc_candle_update', days=1)
def daily_btc_candle_update():
    granularity = 1 * 60 * 60 # 1 hour
    time_delta = dt.timedelta(days=2) # 2 days ago
    start = dt.datetime.utcnow() - time_delta
    end = dt.datetime.utcnow()

    params = dict(start=start, end=end, granularity=granularity)
    data = gdax.get_btc_candles(params)
    influx.write_btc_candles(data)

# updates daily candles for the last week
@sched.scheduled_job('interval', id='weekly_btc_candle_update', days=7)
def weekly_btc_candle_update():
    granularity = 1 * 60 * 60 * 60 # 1 day
    time_delta = dt.timedelta(days=14) # 2 weeks agos
    start = dt.datetime.utcnow() - time_delta
    end = dt.datetime.utcnow()

    params = dict(start=start, end=end, granularity=granularity)
    data = gdax.get_btc_candles(params)
    influx.write_btc_candles(data)

# gets btc ticker for current hour
@sched.scheduled_job('interval', id='update_btc_ticker', hours=1)
def hourly_btc_ticker_update():
   data = gdax.get_btc_ticker()
   influx.write_btc_ticker(data)

sched.start()
