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

@app.route('/')
@app.route('/home')
def hello():
    return render_template("index.html")

#returns manage course page and passes all courses in db
@app.route('/manage-courses')
def manage_courses():
    course_list = list(mongo.db.course.find())
    
    return render_template("manage-courses.html", courses = course_list)


if __name__ == '__main__':
    app.run(host = config.host_val , port = config.port_val, debug=True)