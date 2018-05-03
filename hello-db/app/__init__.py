from flask import Flask
from .jakedb import JakeDB

app = Flask(__name__, template_folder='../templates')
db = JakeDB('data.json')

app.config['SECRET_KEY'] = '123456'

from .views import *