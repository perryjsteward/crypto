from influx_client import InfluxClient
from gdax_client import GdaxClient
import datetime as dt
import dateutil.parser
import time

class DataRefresh(object):

    def __init__(self):
        self._influx = influx = InfluxClient()
        self._gdax = gdax = GdaxClient()
        self._time_delta = 1 * 365 # Number of days ago
        self._granularity = 1 * 60 * 60 # timeslice in seconds
        self._max_candles = 200 # max number returned in request
        self._max_requests = 3 # every second
        self._start = self._format_start() # ISO 8601
        self._end = self._format_end() # ISO 8601
        self._now = dt.datetime.utcnow().isoformat() # complete when start equals now

    def _format_start(self,epoch=None):
        if epoch is None:
            time_delta = dt.timedelta(days=self._time_delta) # 1 year ago
            start_date = dt.datetime.utcnow() - time_delta # Start date

            return start_date.isoformat()

        elif epoch:
            start_date = dt.datetime.utcfromtimestamp(epoch)
            return start_date.isoformat()

    def _format_end(self):
        seconds = self._max_candles * self._granularity # Seconds to add to start
        time_delta = dt.timedelta(seconds=seconds)

        end_date = dateutil.parser.parse(self._start) + time_delta
        return end_date.isoformat()

    def _update_dates(self, data):
        if len(data) == 1:
            self._start = self._end
        else:
            self._start = self._format_start(epoch=data[0][0]) # ISO 8601

        self._end = self._format_end() # ISO 8601

    def _get_historic_candles(self):
        try:
            params = dict(start=self._start, end=self._end, granularity=self._granularity)
            data = self._gdax.get_btc_candles(params=params)
        except:
            print("Error getting data from GDAX")

        # Catches exceed limit
        if 'message'in data:
            print data
            return False

        # Update start and end times
        if len(data) > 0:
            return data

    def _update_historic_data(self, data):
        try:
            print self._start
            self._influx.write_btc_candles(data)
            self._update_dates(data)
        except:
            print("Error pushing to Influx")

    def _get_historic_data(self):
        while self._start < self._now:
            data = self._get_historic_candles()

            # If limit has been reached
            if data is False:
                time.sleep(5)

            elif data is not None:
                self._update_historic_data(data)

    def run(self):
        self._get_historic_data()

# run the file
if __name__ == '__main__':
    print("Running DataRefresh()")

    db_refresh = DataRefresh()
    db_refresh.run()
