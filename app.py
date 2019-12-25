# imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# instantiate the app
app =  Flask(__name__)
# app config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# instantiate db
db = SQLAlchemy(app)

migrate = Migrate(app, db) 

# create model class
class TestTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    string_field = db.Column(db.String(80))
    text_field = db.Column(db.Text)
    date_field = db.Column(db.DateTime)
    float_field = db.Column(db.Float)
    boolean_field = db.Column(db.Boolean)
    # added_string_field = db.Column(db.String(80))

if __name__ == '__main__':
    app.run(debug=True)