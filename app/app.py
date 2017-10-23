# from flask import Flask
# import time
# import crypto_tasks
#
# app = Flask(__name__)
#
# # Can add more routes in here to create an API for querying data from influx or an exchange
# @app.route("/")
# def index():
#     return "{ 'status' : 'ok', 'message' : 'flask is running'}"
#
# if __name__ == "__main__":
#     app.run(use_reloader=False)
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello world!"

if __name__ == "__main__":
    app.run()
