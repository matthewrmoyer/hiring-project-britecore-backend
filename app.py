from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost:5432/britecore_db' 
db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
                return('INDEX PAGE')


if __name__ == '__main__':
        app.debug = True
        app.run()