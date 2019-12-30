import logging
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def default_route():
    """Default route"""
    return jsonify('hello world')

print(__name__)
print("__main__")

logging.basicConfig(filename='error.log', level=logging.DEBUG)