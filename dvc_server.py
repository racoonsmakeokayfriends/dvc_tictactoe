from bottle import route, run, template, request, static_file
import json

STATE = {}

@route('/write/', method='POST')
def write():
    print(request.json)
    global STATE
    STATE = request.json
    return "Success!"

@route('/read/')
def read():
    global STATE
    return STATE

@route('/')
def home():
    return static_file("index.html", root=".")

run(host='localhost', port=8080)
