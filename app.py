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

"""
Index Page Controller

"""

@app.route('/')
@app.route('/home')
def index():
    course = mongo.db.course
    region = mongo.db.region

    featured_course = Record.return_list(list(course.aggregate([{'$sample': {'size':1}}]))) 

    regions = region.find()
    region_list = Record.return_list(regions)

    top_courses = course.find().sort('num_reviews', -1).limit(3)
    tc_list = Record.return_list(top_courses)




    return render_template("index.html", featured = featured_course[0], regions = region_list, tc_courses = tc_list)


"""
Search Course

"""
#Searches the database using user query and returns listed results
@app.route('/search', methods=['POST','GET'])
def search():

    course= mongo.db.course

    region = request.form.get('region')
    course_name = request.form.get('course_name')
    min_rating = int(request.form.get('min_rating'))

    search_item = Record.search_term(region,course_name,min_rating)

    if search_item != "":
        results = course.find(search_item)
    else:
        results = []
           
    list_of_results = Record.return_list(results)
        

    return render_template('search-results.html', results = list_of_results)

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
    course.update({'_id': ObjectId(course_id)}, data)

    return redirect(url_for('manage_courses'))


"""
Review Management controller

"""
#Retrieves list of all reviews created by user logged in
@app.route('/manage-reviews')
def manage_reviews():
    reviews = mongo.db.review
    review_list = list(reviews.find({"user_id": ObjectId(active_user)}).sort('date', -1))
    #converts the unix time to dd/mm/yy
    updated_reviews = Record.convert_time(review_list)

    list_courseIds = Record.find_course_ids(review_list)
    list_of_courses = []
    for id in list_courseIds:
        course = mongo.db.course
        list_of_courses += course.find({"_id": ObjectId(id)})
    courses = list(list_of_courses)

    return render_template("manage-reviews.html", reviews = updated_reviews, courses = courses)

@app.route('/add-review/<course_id>', methods=['POST','GET'])
def add_review(course_id):
    return render_template("add-review.html", course_id = course_id)

#inserts data from form into the review db
@app.route('/add-review/insert/<course_id>', methods=['POST','GET'])
def insert_review(course_id):
    review = mongo.db.review
    data = Record.create_review_record(request.form,active_user,course_id)
    review.insert_one(data)
    average_review(course_id)
    return redirect(url_for('view_course', course_id = course_id))

#calculates the average score from all reviews associated with the given course_id
def average_review(course_id):
    review = mongo.db.review
    course = mongo.db.course

    list_of_reviews = review.find({"course_id": ObjectId(course_id)})
    review_avg = Record.average_rating(list_of_reviews)
    num_reviews = review.find({"course_id": ObjectId(course_id)}).count()

    course.update_one({"_id": ObjectId(course_id)}, 
    {"$set": {
        "avg_rating": review_avg,
        "num_reviews": num_reviews
        }}, upsert=True)

#loads the edit review page with the relevant record
@app.route('/edit-review/<review_id>', methods=['POST','GET'])
def edit_review(review_id):
    review = mongo.db.review
    selected_review = review.find_one({"_id": ObjectId(review_id)})

    return render_template('edit-review.html', review = selected_review)

#Updates review record and updates average score for course
@app.route('/edit-review/update/<review_id>&<course_id>', methods=['POST','GET'])
def update_review(review_id, course_id):
    review = mongo.db.review
    data = Record.create_review_record(request.form,active_user,course_id)
    review.update({'_id': ObjectId(review_id)}, data)
    average_review(course_id)
    return redirect(url_for('manage_reviews'))

#Deletes the selected review from the collection and updates the avg score for the course
@app.route('/manage-reviews/delete/<review_id>&<course_id>')
def delete_review(review_id,course_id):
    review = mongo.db.review
    review.remove({'_id': ObjectId(review_id)})
    average_review(course_id)
    return redirect(url_for('manage_reviews'))


"""
Course View

"""

@app.route('/view/<course_id>')
def view_course(course_id):
    #Need course record
    #reviews for course limit 5

    course = mongo.db.course
    review = mongo.db.review

    course_data = course.find_one({"_id": ObjectId(course_id)})

    list_of_reviews = review.find({"course_id": ObjectId(course_id)}, limit=5).sort('date', -1)
    updated_reviews = Record.convert_time(list_of_reviews)


    return render_template('course-view.html', course = course_data, reviews = updated_reviews)


#Setting app runtime conditions 
if __name__ == '__main__':
    app.run(host = config.host_val , port = config.port_val, debug=True)





