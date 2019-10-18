import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World Again'

#Flask app run configs
host = os.environ.get('IP')
port = int(os.environ.get('PORT'))
#M_URI = os.environ.get('MONGO_URI')

if __name__ == '__main__':
    app.run(host = host, port = port, debug=True)