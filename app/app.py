from flask import Flask
import time

app = Flask(__name__)

# Can add more routes in here to create an API for querying data from influx
@app.route("/")
def index():
    return "{ 'status' : 'ok', 'message' : 'flask is running'}"

if __name__ == "__main__":
    app.run(use_reloader=False)
