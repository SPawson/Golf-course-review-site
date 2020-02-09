from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username'
    ,validators=[DataRequired(), Length(min=2, max=20)])

    email = StringField('Email'
    ,validators=[DataRequired(), Email()])

    password = PasswordField('Password', validators=[DataRequired(), Length(min=4, max=20)])
   
    confirm_password = PasswordField('Confirm Password',
     validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('Register')

class LoginForm(FlaskForm):
  
    email = StringField('Email'
    ,validators=[DataRequired(), Email()])

    password = PasswordField('Password', validators=[DataRequired()])
    
    remember = BooleanField('Remember Me')

    submit = SubmitField('Login')
class Course(FlaskForm):
    course_name = StringField('Course Name'
    ,validators=[DataRequired(), Length(min=2, max=45)])
    par = IntegerField('Par', validators=[DataRequired()])
    course_description = StringField('Course Name'
    ,validators=[DataRequired(), Length(min=2, max=45)])
    address_line_1 = StringField('Address Line 1'
    ,validators=[DataRequired(), Length(min=2, max=45)])
    address_line_2 = StringField('Address Line 2'
    ,validators=[DataRequired(), Length(min=2, max=45)])
    address_line_3 = StringField('Address Line 3'
    ,validators=[DataRequired(), Length(min=2, max=45)])
    region = SelectField(validators=[DataRequired()])
    postcode = StringField('Postcode'
    ,validators=[DataRequired(), Length(min=2, max=8)])
    course_image = StringField('Course Image'
    ,validators=[DataRequired()])
    affiliate_link = StringField('Affiliate Link'
    ,validators=[DataRequired()])

class Review(FlaskForm):
    review_title = StringField('Title',validators=[DataRequired(), Length(min=3, max=45)])
    review_article = TextAreaField('Review',validators=[DataRequired(), Length(min=5)])
