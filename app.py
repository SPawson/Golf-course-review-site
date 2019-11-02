import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from packages.config.config import *
from packages.common.obj_handling import Record
import json

#Configuration for app instance
config = App_Connection()
app = Flask(__name__)
app.config["MONGO_DBNAME"] = config.db_name
app.config["MONGO_URI"] = config.m_uri
mongo = PyMongo(app)

#Temporary User Login ID var
active_user = "5daaff251c9d440000d69d06"
#Temp Course ID for testing
selected_course = "5dbd85633da78418944a2760"

@app.route('/')
@app.route('/home')
def hello():
    return render_template("index.html")


"""
Golf course management controllers

"""

#returns manage course page and passes all courses in db
@app.route('/manage-courses')
def manage_courses():
    course_list = list(mongo.db.course.find())
    
    return render_template("manage-courses.html", courses = course_list)

#retrieves add course template and popualtes region drop box
@app.route('/add-course')
def add_course():
    regions = mongo.db.region.find()
    region_list = Record.return_list(regions)
    return render_template("add-course.html", regions = region_list)

#Inserts the record into the course DB
@app.route('/add-course/insert', methods=['POST','GET'])
def insert_course():
    course = mongo.db.course
    data = Record.create_course_record(request.form)
    course.insert_one(data)
    return redirect(url_for('manage_courses'))

#Deletes the selected course based on the id passed into the function
@app.route('/manage-courses/delete/<course_id>')
def delete_course(course_id):
    course = mongo.db.course
    course.remove({'_id': ObjectId(course_id)})
    return redirect(url_for('manage_courses'))

#Loads the edit page and populates all the fields based on the record retrieved
@app.route('/manage-courses/edit/<course_id>')
def edit_course(course_id, methods=['POST','GET']):
    regions = mongo.db.region.find()
    region_list = Record.return_list(regions)

    course = mongo.db.course
    selected_course = course.find_one({"_id": ObjectId(course_id)})

    return render_template("edit-course.html", regions = region_list , course = selected_course)

#Updates the existing record based on the information entered into the form
@app.route('/manage-courses/update/<course_id>', methods=['POST','GET'])
def update_course(course_id):
    course = mongo.db.course
    data = Record.create_course_record(request.form)
    print(data)
    course.update({'_id': ObjectId(course_id)}, data)

    return redirect(url_for('manage_courses'))


"""
Review Management controller

"""
#Retrieves list of all reviews created by user logged in
@app.route('/manage-reviews')
def manage_reviews():
    reviews = mongo.db.review
    review_list = list(reviews.find({"user_id": ObjectId(active_user)}))
    print("Tests")

    list_courseIds = Record.find_value(review_list, "course_id")

    list_of_courses = []
    for id in list_courseIds:
        course = mongo.db.course
        list_of_courses += course.find({"_id": ObjectId(id)})
        print(id)
    
    courses = list(list_of_courses)

    #updated_course = Record.convert_time(courses)
        
    return render_template("manage-reviews.html", reviews = review_list, courses = courses)

@app.route('/add-review')
def add_review():

    return render_template("add-review.html")

@app.route('/add-review/insert', methods=['POST','GET'])
def insert_review():
    review = mongo.db.review
    data = Record.create_review_record(request.form,active_user,selected_course)
    review.insert_one(data)
    average_review(selected_course)
    return redirect(url_for('manage_reviews'))

#Setting app runtime conditions 
if __name__ == '__main__':
    app.run(host = config.host_val , port = config.port_val, debug=True)


def average_review(course_id):
    review = mongo.db.review
    course = mongo.db.course

    list_of_reviews = review.find({"course_id": ObjectId(course_id)})
    review_avg = Record.average_rating(list_of_reviews)

    course.update_one({"_id": ObjectId(course_id)}, 
    {
        "avg_rating": review_avg
    }
    )



