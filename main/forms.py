# from unicodedata import name

from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_wtf.file import FileField, FileAllowed
from main.models import Visitor, Hospital, Place

#forms for registration
#agents are entered(registered) manually through db terminal
class regvisitor(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    address = StringField ('Address', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    number=StringField('Phone', validators=[DataRequired()])
    device_id=StringField('Device ID', validators=[DataRequired()])
    submit = SubmitField('Sign Up')
    
    #validation functions are made for checking the uniqueness of data

    def validate_email(self, email):
        visit1=Visitor.query.filter_by(email=email.data).first()

        if visit1:
            raise ValidationError('Email already registered')

    def validate_number(self, number):
        visit2=Visitor.query.filter_by(phone=number.data).first()

        if visit2:
            raise ValidationError('Phone already registered')

    def validate_device_id(self, device_id):
        visit3=Visitor.query.filter_by(device_id=device_id.data).first()

        if visit3:
            raise ValidationError('Device ID already registered')

class update_visitor_account(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    address = StringField ('Address', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    phone=StringField('Phone', validators=[DataRequired()])
    device_id=StringField('Device ID', validators=[DataRequired()])
    image_file=FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')
    
    #validation functions are made for checking the uniqueness of data

    def validate_email(self, email):
        if email.data != current_user.email:
            visit1=Visitor.query.filter_by(email=email.data).first()

            if visit1:
                raise ValidationError('Email already registered')

    def validate_phone(self, phone):
        if phone.data != current_user.phone:
            visit2=Visitor.query.filter_by(phone=phone.data).first()

            if visit2:
                raise ValidationError('Phone already registered')

    def validate_device_id(self, device_id):
        if device_id.data != current_user.device_id:
            visit3=Visitor.query.filter_by(device_id=device_id.data).first()

            if visit3:
                raise ValidationError('Device ID already registered')

class update_place_account(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    address = StringField ('Address', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    phone=StringField('Phone', validators=[DataRequired()])
    submit = SubmitField('Update')
    
    #validation functions are made for checking the uniqueness of data

    def validate_email(self, email):
        if email.data != current_user.email:
            visit1=Place.query.filter_by(email=email.data).first()

            if visit1:
                raise ValidationError('Email already registered')

    def validate_phone(self, phone):
        if phone.data != current_user.phone:
            visit2=Place.query.filter_by(phone=phone.data).first()

            if visit2:
                raise ValidationError('Phone already registered')

class regplace(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    address = StringField ('Address', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    number=StringField('Phone', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        place1=Place.query.filter_by(email=email.data).first()

        if place1:
            raise ValidationError('Email already registered')

    def validate_number(self, number):
        place2=Place.query.filter_by(phone=number.data).first()

        if place2:
            raise ValidationError('Phone already registered')

class reghospital(FlaskForm):
    name=StringField('name',validators=[DataRequired()])
    email=StringField('Email', validators=[DataRequired()])
    reg=StringField('reg', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    address = StringField ('Address', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        hos1=Hospital.query.filter_by(email=email.data).first()

        if hos1:
            raise ValidationError('Email already registered')

    def validate_reg(self, reg):
        hos2=Hospital.query.filter_by(license=reg.data).first()

        if hos2:
            raise ValidationError('License no. already registered')

#forms for logging in             
class vislogin(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class hospitallogin(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    # remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class placelogin(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    # remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class agentlogin(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    # remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
