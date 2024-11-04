from flask import Flask

app = Flask(__name__)

endpoint_counter = 0

@app.route('/hello/world')
def hello_world():
    return 'Hello world'

@app.route('/counter')
def counter():
    global endpoint_counter
    endpoint_counter += 1
    return str(endpoint_counter)