from flask import Flask
#from config import Config # si la config est définie dans config.py
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)


#from app import routes, models 