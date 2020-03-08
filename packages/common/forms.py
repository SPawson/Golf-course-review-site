from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo

#Controls validation for registration form
class RegistrationForm(FlaskForm):
    username = StringField('Username'
    ,validators=[DataRequired(), Length(min=2, max=20)])

    email = StringField('Email'
    ,validators=[DataRequired(), Email()])

    password = PasswordField('Password', validators=[DataRequired(), Length(min=4, max=20)])
   
    confirm_password = PasswordField('Confirm Password',
     validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('Register')

#Controls validation for Login form
class LoginForm(FlaskForm):
  
    email = StringField('Email'
    ,validators=[DataRequired(), Email()])

    password = PasswordField('Password', validators=[DataRequired()])
    
    remember = BooleanField('Remember Me')

    submit = SubmitField('Login')

#Controls validation for Course form
class Course(FlaskForm):
    course_name = StringField('Course Name'
    ,validators=[DataRequired("A valid number must be used"), Length(min=3, max=90)])
    par = IntegerField('Par', validators=[DataRequired()])
    description = TextAreaField('Description'
    ,validators=[DataRequired(), Length(min=3)])
    address_line_1 = StringField('Address Line 1'
    ,validators=[DataRequired(), Length(min=3, max=70)])
    address_line_2 = StringField('Address Line 2'
    ,validators=[DataRequired(), Length(min=3, max=70)])
    address_line_3 = StringField('Address Line 3')
    postcode = StringField('Postcode'
    ,validators=[DataRequired(), Length(min=6, max=8)])
    course_img = StringField('Course Image'
    ,validators=[DataRequired()])
    affiliate_link = StringField('Affiliate Link'
    ,validators=[DataRequired()])

#Course object used for the preloading of course data
class CourseObj():
    def __init__(self):
        self.course_name = None
        self.par = None
        self.description = None
        self.address_line_1 = None
        self.address_line_2 = None
        self.address_line_3 = None
        self.postcode = None
        self.course_img = None
        self.affiliate_link = None

#Controls validation for the review form
class Review(FlaskForm):
    review_title = StringField('Title',validators=[DataRequired(), Length(min=3, max=45)])
    review_article = TextAreaField('Review',validators=[DataRequired(), Length(min=5)])

#Review object used for preloading the review data
class ReviewObj():
    def __init__(self):
        self.review_title = None
        self.review_article = None
        


   





    
    

