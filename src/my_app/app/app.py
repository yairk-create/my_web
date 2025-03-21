#!/home/yair/project/my_web/bin/python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World"

@app.route('/<name>')
def hello(name): 
    return f'Hello {name}'


# app.run(port=8000)
app.run(host='0.0.0.0', port=8000,debug=True)


