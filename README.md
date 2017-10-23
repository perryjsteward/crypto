# crypto_tracker

### Dependencies
- Influx instance (need one running)
- Python 2.7
- PIP (Pithon package manager)


### Setup
1. create a python virtual environment: virtualenv venv
2. activate environment: source venv/bin/activate
3. install requirements: pip install -r requirements.txt
4. install system requirements: sudo apt-get install $(cat requirements.system)
4. update '.env.in' with influx info and rename to '.env'
5. to run flask app in DEBUG: python app/app.py
6. navigate to localhost:5000 to check if its working
