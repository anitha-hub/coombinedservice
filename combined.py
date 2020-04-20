import json

from flask import Flask
from flask import jsonify
from flask_pymongo import PyMongo
import requests
from bson.json_util import dumps


app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'user_service'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/user_service'
mongo = PyMongo(app)

@app.route('/user/<name>/post',methods=['GET'])
def add_user(name):
    PARAMS = {'name': name}
    post = requests.get("http://127.0.0.1:5002/posts/{}".format(name))
    user = requests.get("http://127.0.0.1:5001/users/{}".format(name))
    post_list = post.json()
    users = user.json()
    z = dict(list(post_list.items()) + list(users.items()))
    return dumps(z)

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000,debug=True)