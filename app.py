import os
from flask import Flask, render_template, flash ,redirect, request, url_for, session
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from bson.objectid import ObjectId
from packages.config.config import *
from packages.common.obj_handling import Record
from packages.common.forms import RegistrationForm, LoginForm, Course, Review, CourseObj
from packages.search.search import Pagination, Search
import math

from flask_login import LoginManager, UserMixin, current_user
import json

#Configuration for app instance
config = App_Connection()
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config["MONGO_DBNAME"] = config.db_name
app.config["MONGO_URI"] = config.m_uri
app.config["SECRET_KEY"] = config.secret_key
app.config['DEBUG'] = True
mongo = PyMongo(app)

#Database names
user_db = mongo.db.user
course_db = mongo.db.course
region_db = mongo.db.region
review_db = mongo.db.review

"""
Index Page Controller

"""

@app.route('/')
@app.route('/home')
def index():
    
    featured_course = Record.return_list(list(course_db.aggregate([{'$sample': {'size':1}}]))) 

    regions = region_db.find()
    region_list = Record.return_list(regions)

    top_courses = course_db.find().sort('num_reviews', -1).limit(3)
    tc_list = Record.return_list(top_courses)

    return render_template("index.html", featured = featured_course[0], regions = region_list, tc_courses = tc_list)


"""
Search Course

"""
#Searches the database using user query and returns listed results
@app.route('/search/<searching>/<dir>', methods=['POST','GET'])
def search(searching,dir):
    if searching == 'True':
        region = request.form.get('region')
        course_name = request.form.get('course_name')
        min_rating = int(request.form.get('min_rating'))
        session["search_item"] = Search.search_term(region,course_name,min_rating)
        session["skip"] = 0

    limit=4
    if dir == 'next':
        session["skip"] += 1 
    elif dir == 'prev':
        session["skip"] -= 1  

    if session["search_item"] != "":
        count = course_db.count(session["search_item"])
        pagination = Pagination(limit,count,session["skip"])
        pagination.results = Record.return_list(course_db.find(session["search_item"]).skip(pagination.skips).limit(pagination.limit))
    else:
        count = course_db.count()
        pagination = Pagination(limit,count,session["skip"])
        pagination.results = Record.return_list(course_db.find().sort('num_reviews', -1).skip(pagination.skips).limit(pagination.limit)) 
    
    return render_template('search-results.html', pagination = pagination)


    

"""
Registration/Login Controllers

"""
@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()       
    if form.validate_on_submit():
        if does_email_exist(form.email.data):
            flash(f'Account with email {form.email.data} exists', 'card-panel teal lighten-2')
            return redirect(url_for('register'))
        else:
            secure_password = bcrypt.generate_password_hash(form.password.data).decode('utf8')
            data = Record.create_user_record(request.form, secure_password)
            user_db.insert_one(data)
            flash(f'Account created for {form.username.data}!', 'card-panel teal lighten-2')
            return redirect(url_for('login'))

    return render_template('register.html', title = 'Register', form=form)
#Determines if the email exists
def does_email_exist(search_item):
    result = user_db.find_one({'email':search_item})
    if not result:
        return False
    else:
        return True 


#logs in the user and sets the session variables
@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user_record = user_db.find_one({'email':form.email.data})
        user_email =  ""
        user_password = ""
        if user_record:
            user_email =  user_record["email"]
            user_password = user_record["password"]

        if form.email.data == user_email and bcrypt.check_password_hash(user_password, form.password.data):
            session["user_id"] = str(user_record["_id"])
            session["username"] = user_record["username"]
            session["logged_in"] = True
            session["is_admin"] = user_record["is_admin"]
            return redirect(url_for('index'))
        else:
            flash('Login Unsuccesfull, please check email and password', 'card-panel teal lighten-2')
            return render_template('login.html', title = 'Login', form=form)

    else:
        return render_template('login.html', title = 'Login', form=form)


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    session.pop('logged_in', None)
    session.pop('is_admin', None)
    return redirect(url_for('index'))


"""
Golf course management controllers

"""

#returns manage course page and passes all courses in db
@app.route('/manage-courses/<load>/<dir>')
def manage_courses(load,dir):

    if load == 'True':
        session["skip"] = 0
    
    limit=5
    if dir == 'next':
        session["skip"] += 1 
    elif dir == 'prev':
        session["skip"] -= 1 

    count = course_db.count()
    pagination = Pagination(limit,count,session["skip"])
    pagination.results = course_db.find().skip(pagination.skips).limit(pagination.limit)
    
    return render_template("manage-courses.html", pagination = pagination)

#retrieves add course template and popualtes region drop box

@app.route('/add-course', methods=['POST','GET'])
def add_course():
    if session["logged_in"]:
        form = Course()
        regions = region_db.find()
        region_list = Record.return_list(regions)

        if form.validate_on_submit():
            data = Record.create_course_record(request.form)
            course_db.insert_one(data)
            return redirect(url_for('manage_courses'))

        return render_template("add-course.html", regions = region_list, form = form)
    else:
        return redirect(url_for("index"))

#Deletes the selected course based on the id passed into the function
@app.route('/manage-courses/delete/<course_id>')
def delete_course(course_id):
    course_db.remove({'_id': ObjectId(course_id)})
    return redirect(url_for('manage_courses'))

#Loads the edit page and populates all the fields based on the record retrieved
@app.route('/manage-courses/edit/<course_id>')
def edit_course(course_id, methods=['POST','GET']):
    if session["logged_in"]:
        regions = region_db.find()
        region_list = Record.return_list(regions)
        selected_course = course_db.find_one({"_id": ObjectId(course_id)})
        selected_region = Record.find_single_value(selected_course, "region")
        form_data = Record.prepopulate_course_form(selected_course)
        form = Course(obj = form_data)


        return render_template("edit-course.html", regions = region_list , course = selected_course, form = form, selected_region=selected_region)
            
    else:
        return redirect(url_for("index"))


    

#Updates the existing record based on the information entered into the form
@app.route('/manage-courses/update/<course_id>', methods=['POST','GET'])
def update_course(course_id):
    if session["logged_in"]:
        form = Course()
        regions = region_db.find()
        region_list = Record.return_list(regions)
        
        selected_course = course_db.find_one({"_id": ObjectId(course_id)})
        selected_region = Record.find_single_value(selected_course, "region")
        if form.validate_on_submit():
            data = Record.create_course_record(request.form)
            course_db.update({'_id': ObjectId(course_id)}, data)
            return redirect(url_for('manage_courses'))
        else:
            return render_template("edit-course.html", regions = region_list , course = selected_course, form = form, selected_region=selected_region)
    else:
        return redirect(url_for('manage_courses'))


"""
Review Management controller

"""
#Retrieves list of all reviews created by user logged in
@app.route('/manage-reviews/<load>/<dir>')
def manage_reviews(load,dir):
    review_list = list(review_db.find({"user_id": ObjectId(session["user_id"])}).sort('date', -1))
    #converts the unix time to dd/mm/yy
    updated_reviews = Record.convert_time(review_list)

    if load == 'True':
        session["skip"] = 0

    limit=8
    if dir == 'next':
        session["skip"] += 1 
    elif dir == 'prev':
        session["skip"] -= 1

    count = len(updated_reviews)
    pagination = Pagination(limit,count,session["skip"])
    pagination.results = updated_reviews

    list_courseIds = Record.find_course_ids(review_list)
    list_of_courses = []
    for id in list_courseIds:
        list_of_courses += course_db.find({"_id": ObjectId(id)})

    courses = list(list_of_courses)

    return render_template("manage-reviews.html", pagination = pagination, courses = courses)

#inserts data from form into the review db
@app.route('/add-review/<course_id>', methods=['POST','GET'])
def add_review(course_id):
    if session["logged_in"]:
        form = Review()
        if form.validate_on_submit():
             data = Record.create_review_record(request.form, session["user_id"],course_id, session["username"])
             review_db.insert_one(data)
             average_review(course_id)
             return redirect(url_for("manage_reviews" , load= True ,dir=False))
        else:
            return render_template("add-review.html", course_id = course_id, form=form)
    
    else:
        return redirect(url_for('view_course', course_id = course_id))
        



#calculates the average score from all reviews associated with the given course_id
def average_review(course_id):
    list_of_reviews = review_db.find({"course_id": ObjectId(course_id)})
    review_avg = Record.average_rating(list_of_reviews)
    num_reviews = review_db.find({"course_id": ObjectId(course_id)}).count()

    course_db.update_one({"_id": ObjectId(course_id)}, 
    {"$set": {
        "avg_rating": review_avg,
        "num_reviews": num_reviews
        }}, upsert=True)

#loads the edit review page with the relevant record
@app.route('/edit-review/<review_id>', methods=['POST','GET'])
def edit_review(review_id):
    selected_review = review_db.find_one({"_id": ObjectId(review_id)})
    form_data = Record.prepopulate_review_form(selected_review)
    form = Review(obj = form_data)

    return render_template('edit-review.html', review = selected_review, form= form)


#Updates review record and updates average score for course
@app.route('/edit-review/update/<review_id>&<course_id>', methods=['POST','GET'])
def update_review(review_id, course_id):
    data = Record.create_review_record(request.form,session["user_id"],course_id,session["username"] )
    review_db.update({'_id': ObjectId(review_id)}, data)
    average_review(course_id)
    return redirect(url_for('manage_reviews', load= True ,dir=False))

#Deletes the selected review from the collection and updates the avg score for the course
@app.route('/manage-reviews/delete/<review_id>&<course_id>')
def delete_review(review_id,course_id):
    review_db.remove({'_id': ObjectId(review_id)})
    average_review(course_id)
    return redirect(url_for('manage_reviews', load= True ,dir=False))


"""
Course View

"""

@app.route('/view/<load>/<dir>/<course_id>')
def view_course(load,dir,course_id):

    if load == 'True':
        session["skip"] = 0
    
    limit=4
    if dir == 'next':
        session["skip"] += 1 
    elif dir == 'prev':
        session["skip"] -= 1 

    course_data = course_db.find_one({"_id": ObjectId(course_id)})

    list_of_reviews = review_db.find({"course_id": ObjectId(course_id)}, limit=5).sort('date', -1)
    updated_reviews = Record.convert_time(list_of_reviews)

    count = len(updated_reviews)
    pagination = Pagination(limit,count,session["skip"])
    pagination.results = updated_reviews

    return render_template('course-view.html', course = course_data, pagination = pagination)



#Setting app runtime conditions 
if __name__ == '__main__':
    app.run(host = config.host_val , port = config.port_val, debug=True)





