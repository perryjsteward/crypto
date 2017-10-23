import sys
import os

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + '/crypto/app')

activate_this = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + '/crypto/venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

from app import app as application
