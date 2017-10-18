from flask import Flask
import time
from apscheduler.scheduler import Scheduler

app = Flask(__name__)

def test_scheduler():
     print "TEST"
     print time.time()


# Can add more routes in here to create an API for querying data from influx
@app.route("/")
def index():
    return "{ 'status' : 'ok', 'message' : 'flask is running'}"

if __name__ == "__main__":
    app.run(use_reloader=False)
