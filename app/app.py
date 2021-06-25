import os
from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
import time

from pymongo import MongoClient

application = Flask(__name__)

application.config["MONGO_URI"] = 'mongodb://' + os.environ['MONGODB_USERNAME'] + ':' + \
    os.environ['MONGODB_PASSWORD'] + '@' + os.environ['MONGODB_HOSTNAME'] + \
    ':27017/' + os.environ['MONGODB_DATABASE']

mongo = PyMongo(application)
db = mongo.db


@application.route('/')
def index():
    username = os.environ['MONGODB_USERNAME']
    password = os.environ['MONGODB_PASSWORD']
    tic = time.perf_counter()
    client = MongoClient('mongo', 27017, username=username, password=password)
    toc = time.perf_counter()
    print(f"Get client login in {toc - tic:0.4f} seconds")

    tic = time.perf_counter()
    list(client.list_databases())
    toc = time.perf_counter()
    print(f"Get list client login in {toc - tic:0.4f} seconds")

    return jsonify(
        status=True,
        message='Welcome to the Dockerized Flask MongoDB app!'
    )


@application.route('/todo')
def todo():
    _todos = db.todo.find()

    item = {}
    data = []
    for todo in _todos:
        item = {
            'id': str(todo['_id']),
            'todo': todo['todo']
        }
        data.append(item)

    return jsonify(
        status=True,
        data=data
    )


@application.route('/todo', methods=['POST'])
def createTodo():
    data = request.get_json(force=True)
    item = {
        'todo': data['todo']
    }
    db.todo.insert_one(item)

    return jsonify(
        status=True,
        message='To-do saved successfully!'
    ), 201