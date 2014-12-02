from flask import Flask 
# For this example we'll use SQLAlchemy, a popular ORM that supports a 
# variety of backends including SQLite, MySQL, and PostgreSQL 
from flask.ext.sqlalchemy import SQLAlchemy 
app = Flask(__name__) 
# We'll just use SQLite here so we don't need an external database 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' 
db = SQLAlchemy(app)
