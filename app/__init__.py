from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import SQLALCHEMY_BINDS

# init flask obj
app = Flask(__name__)
# bind config of the MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_BINDS['mysql']

db = SQLAlchemy(app)

