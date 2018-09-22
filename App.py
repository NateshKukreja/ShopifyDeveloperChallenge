from flask import Flask
import pymongo


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/')
def return_world():
    return 'heeeeeeeelloo'

def populateDB():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    mycol = mydb["customers"]
    
def populateShops():
    return

def populateOrders():
    return

def populateProducts():
    return

def populateLineItems():
    return