import core.alpengo_data as alpengo_data
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.getcwd()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{basedir}/alpengo.db"
app.config['SECRET_KEY'] = '36e37b21094cafe5ecdfe25318e6e991'
db = SQLAlchemy(app)

from core import routes