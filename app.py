import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from packages.config.config import *


#Configuration for app instance
config = App_Connection()
app = Flask(__name__)
app.config["MONGO_DBNAME"] = config.db_name
app.config["MONGO_URI"] = config.m_uri





@app.route('/')
def hello():
    return 'Hello World Again'

#Flask app run configs

if __name__ == '__main__':
    app.run(host = config.host_val , port = config.port_val, debug=True)