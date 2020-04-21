from flask import Flask
import requests
from flask import request
from bson.json_util import dumps

app = Flask(__name__)

@app.route('/user/<name>/post',methods=['GET'])
def getuserdetails(name):
    post = requests.get("http://127.0.0.1:5002/posts/{}".format(name))
    user = requests.get("http://127.0.0.1:5001/users/{}".format(name))
    post_list = post.json()
    users = user.json()
    z = dict(list(post_list.items()) + list(users.items()))
    return dumps(z)

@app.route('/user',methods=['GET','POST'])
def adduser():
    if request.method == 'GET':
        user = requests.get("http://127.0.0.1:5001/users")
        users = user.json()
        return dumps(users)
    if request.method == 'POST':
        name = request.json['name']
        mobileno = request.json['mobileno']
        aadhaarno = request.json['aadhaarno']
        email = request.json['email']
        address = request.json['address']
        data={'name':name,'mobileno':mobileno,'aadhaarno':aadhaarno,'email':email,'address':address}
        api_url="http://127.0.0.1:5001/adduser"
        user = requests.post(url=api_url,json=data)
        return user.text

@app.route('/user/<id>',methods=['GET','PUT','DELETE'])
def updateuser(id):
    if request.method == 'GET':
        response = requests.get("http://127.0.0.1:5001/oneuser/{}".format(id))
        return response.text
    if request.method == 'PUT':
        name = request.json['name']
        mobileno = request.json['mobileno']
        aadhaarno = request.json['aadhaarno']
        email = request.json['email']
        address = request.json['address']
        data = {'name': name, 'mobileno': mobileno, 'aadhaarno': aadhaarno, 'email': email, 'address': address}
        api_url = "http://127.0.0.1:5001/update/{}"
        updateuser = requests.put(url=api_url.format(id), json=data)
        return updateuser.text
    if request.method == 'DELETE':
        response = requests.delete("http://127.0.0.1:5001/delete/{}".format(id))
        return response.text

@app.route('/post',methods=['GET','POST'])
def addpost():
    if request.method == 'GET':
        user = requests.get("http://127.0.0.1:5002/posts")
        users = user.json()
        return dumps(users)
    if request.method == 'POST':
        name = request.json['name']
        post = request.json['post']
        data = {'name': name, 'post': post}
        api_url = "http://127.0.0.1:5002/addpost"
        post = requests.post(url=api_url, json=data)
        return post.text

@app.route('/post/<id>',methods=['GET','PUT','DELETE'])
def updatepost(id):
    if request.method == 'GET':
        response = requests.get("http://127.0.0.1:5002/onepost/{}".format(id))
        return response.text
    if request.method == 'PUT':
        name = request.json['name']
        post = request.json['post']
        data = {'name': name, 'post': post}
        api_url = "http://127.0.0.1:5002/updatepost/{}"
        updatepost = requests.put(url=api_url.format(id), json=data)
        return updatepost.text
    if request.method == 'DELETE':
        response = requests.delete("http://127.0.0.1:5002/deletepost/{}".format(id))
        return response.text

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000,debug=True)