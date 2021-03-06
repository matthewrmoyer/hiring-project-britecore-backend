from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost:5432/britecore_db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)    
    email = db.Column(db.String)

class RiskTypes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String)    
    user = db.Column(db.String)

class RiskFields(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)    
    risk_type = db.Column(db.String)
    data_type = db.Column(db.String)

if __name__ == '__main__':
    manager.run()
