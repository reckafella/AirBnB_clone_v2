#!/usr/bin/python3
''' Module to run the Flask web app on 0.0.0.0:5000 '''
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
	return "<p>Hello, HBNB!</p>"
@app.run(host='0.0.0.0', port=5000)
