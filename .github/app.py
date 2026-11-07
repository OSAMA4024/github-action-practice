# #this commint the first code
# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return render_template('index.html')

# @app.route('/health')
# def health():
#     return 'Server is up and running'
import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    print("Hello Osama")
    x = 10
    y = 20
    return render_template('index.html')

@app.route('/health')
def health():
    return 'Server is up and running'

def unused_function():
    a = 10
    b = 20
