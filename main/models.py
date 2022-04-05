from email.policy import default
from main import db, login_manager
from flask_login import UserMixin
from flask import session

#login manager is used to know the current status of user
@login_manager.user_loader
def load_user(user_id):
    if session["userType"]=="visitor":
        return Visitor.query.get(int(user_id))
    if session["userType"]=="place":
        return Place.query.get(int(user_id))
    if session["userType"]=="agent":
        return Agent.query.get(int(user_id))
    if session["userType"]=="hospital":
        return Hospital.query.get(int(user_id))
    
#classes here are made for tables in databases

class Visitor(db.Model, UserMixin):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(50), nullable=False)
    email=db.Column(db.String(120), unique=True, nullable=False)
    image_file=db.Column(db.String(500), nullable=False, default='default.jpg')
    password=db.Column(db.String(60), nullable=False)
    phone=db.Column(db.String(15), nullable=False)
    city=db.Column(db.String(25), nullable=False)
    address=db.Column(db.String(25), nullable=False)
    device_id=db.Column(db.String(10), nullable=False)
    is_infected=db.Column(db.Integer, nullable=False, default=0)

    # relationship, are yet to be kept

    #these sort of syntax are return at end of each table so that we can view data in python3 terminal
    def __repr__(self):
        return f"Visitor('{self.name}','{self.email}', '{self.phone}', '{self.city}', '{self.image_file}, '{self.is_infected}')"
 
    def get_id(self):
        return self.id

class Place(db.Model, UserMixin):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(20), nullable=False)
    email=db.Column(db.String(120), unique=True, nullable=False)
    password=db.Column(db.String(60), nullable=False)
    phone=db.Column(db.String(15), nullable=False)
    city=db.Column(db.String(25), nullable=False)
    address=db.Column(db.String(25), nullable=False)
    # relationship, qrcode are yet to be kept

    def __repr__(self):
        return f"Place('{self.name}','{self.email}', '{self.phone}', '{self.city}')"
    
    def get_id(self):
        return self.id

class Hospital(db.Model, UserMixin):
    id=db.Column(db.Integer, primary_key=True)
    license= db.Column(db.String(15), nullable=False)
    name=db.Column(db.String(20), nullable=False)
    email=db.Column(db.String(120), unique=True, nullable=False)
    phone=db.Column(db.String(15), nullable=False)
    city=db.Column(db.String(25), nullable=False)
    address=db.Column(db.String(25), nullable=False)
    password=db.Column(db.String(60), nullable=True)
    is_approved=db.Column(db.Integer, nullable=False, default=0)

    def __repr__(self):
        return f"Hospital('{self.name}','{self.license}', '{self.password}','{self.email}', '{self.city}', {self.is_approved})"

    def get_id(self):
        return self.id

class Agent(db.Model, UserMixin):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(20), nullable=False)
    email=db.Column(db.String(120), unique=True, nullable=False)
    password=db.Column(db.String(60), nullable=False)
    phone=db.Column(db.String(15), nullable=False)
    city=db.Column(db.String(25), nullable=False)
    address=db.Column(db.String(25), nullable=False)    

    def __repr__(self):
        return f"Agent('{self.name}','{self.email}', '{self.phone}', '{self.city}')"
 
    def get_id(self):
        return self.id
    
    ##more relationship tables and some columns are to be added while we progress on adding functionalities
