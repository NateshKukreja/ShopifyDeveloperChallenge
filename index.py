from flask import Flask
import pymongo
import json
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)

@app.route('/')
def home_page():
    return "hello"

@app.route('/api/v1.0', methods=['GET'])
def dummy_endpoint():
    return json.dumps({'data': 'Server running'}), 200

def init_db():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    mycol = mydb["customers"]
    return mycol
