from flask import Flask
import requests
from flask import request
from bson.json_util import dumps
from requests.auth import HTTPBasicAuth



app = Flask(__name__)

# @app.route('/user/<name>/post',methods=['GET'])
# def getuserdetails(name):
#     post = requests.get("http://127.0.0.1:5002/posts/{}".format(name))
#     user = requests.get("http://127.0.0.1:5001/users/{}".format(name))
#     post_list = post.json()
#     users = user.json()
#     z = dict(list(post_list.items()) + list(users.items()))
#     return dumps(z)

@app.route('/login',methods=['GET','POST'])
def login():
        auth = request.authorization
        username = auth.username
        password = auth.password
        api_url = "http://127.0.0.1:5001/login"
        user = requests.post(url=api_url,auth=HTTPBasicAuth(username, password))
        return user.text

@app.route('/users',methods=['GET','POST'])
def adduser():
    headers=request.headers
    if request.method == 'GET':
        user = requests.get("http://127.0.0.1:5001/users",headers=headers)
        users = user.json()
        return dumps(users)
    if request.method == 'POST':
        username = request.json['username']
        mobileno = request.json['mobileno']
        aadhaarno = request.json['aadhaarno']
        email = request.json['email']
        address = request.json['address']
        password=request.json['password']
        data={'username':username,'password':password,'mobileno':mobileno,'aadhaarno':aadhaarno,'email':email,'address':address}
        api_url="http://127.0.0.1:5001/register"
        user = requests.post(url=api_url,json=data,headers=headers)
        return user.text

@app.route('/user',methods=['GET','PUT','DELETE'])
def updateuser():
    headers=request.headers
    if request.method == 'GET':
        response = requests.get("http://127.0.0.1:5001/oneuser",headers=headers)
        return response.text
    if request.method == 'PUT':
        username = request.json['username']
        mobileno = request.json['mobileno']
        aadhaarno = request.json['aadhaarno']
        email = request.json['email']
        address = request.json['address']
        password=request.json['password']
        data = {'username': username, 'password': password,'mobileno': mobileno, 'aadhaarno': aadhaarno, 'email': email, 'address': address}
        api_url = "http://127.0.0.1:5001/update"
        updateuser = requests.put(url=api_url, json=data,headers=headers)
        return updateuser.text
    if request.method == 'DELETE':
        response = requests.delete("http://127.0.0.1:5001/delete",headers=headers)
        return response.text

@app.route('/post',methods=['GET','POST'])
def addpost():
    if request.method == 'POST':
        headers=request.headers
        name = request.json['name']
        post = request.json['post']
        data = {'name': name, 'post': post}
        api_url = "http://127.0.0.1:5002/addpost"
        post = requests.post(url=api_url, json=data,headers=headers)
        return post.text

@app.route('/postdetails/<id>',methods=['GET','PUT','DELETE'])
def updatepost(id):
    headers=request.headers
    if request.method == 'GET':
        response = requests.get("http://127.0.0.1:5002/post",headers=headers)
        return response.text
    if request.method == 'PUT':
        name = request.json['name']
        post = request.json['post']
        data = {'name': name, 'post': post}
        api_url = "http://127.0.0.1:5002/updatepost"
        updatepost = requests.put(url=api_url, json=data,headers=headers)
        return updatepost.text
    if request.method == 'DELETE':
        response = requests.delete("http://127.0.0.1:5002/deletepost/{}".format(id),headers=headers)
        return response.text

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)