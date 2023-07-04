from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask import render_template


app = Flask(__name__)
app.config.from_object(Configuration)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///medicalDB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



class Users(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    psw = db.Column(db.String(500), nullable=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<users {self.id}>"


class Profiles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    old = db.Column(db.Integer)
    city = db.Column(db.String(100))

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f"<profiles {self.id}>"

with app.app_context():
    db.create_all()


if __name__ == '__main__':
    from view import app
    app.run(debug=True)
