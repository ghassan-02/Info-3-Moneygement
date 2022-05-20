from . import db
from flask_login import UserMixin #custom class helps for login
from sqlalchemy.sql import func
import datetime


class User(db.Model, UserMixin): #databse layout
    id=db.Column(db.Integer,primary_key=True)
    firstname=db.Column(db.String(150))
    lastname=db.Column(db.String(150))
    email=db.Column(db.String(150),unique=True)
    phone=db.Column(db.Integer)
    password=db.Column(db.String(150))
    country=db.Column(db.String(150))
    accounts=db.relationship('Account')
    payments=db.relationship('Payment')
    inbox=db.relationship('Message')
    payments_history=db.relationship('Payments_history') 

class Account(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(150))
    type=db.Column(db.String(150))
    currency=db.Column(db.String(150))
    balance=db.Column(db.Integer)
    description=db.Column(db.String(150))
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'))

class Payment(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    amount=db.Column(db.Integer)
    type=db.Column(db.String(150))
    period=db.Column(db.String(150))
    currency=db.Column(db.String(150))
    duedate=db.Column(db.Date)
    description=db.Column(db.String(150))
    payment_accountid=db.Column(db.Integer)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'))

class Message(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    sender_name=db.Column(db.String(150))
    content=db.Column(db.String(300))
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'))

class Payments_history(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    amount=db.Column(db.Integer)
    currency=db.Column(db.String(150))
    paiddate=db.Column(db.Date)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'))