#!/usr/bin/python3
""" flask script """

from flask import Flask


app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_route():
	"""
	This is a route that will be called when the application is initialized
    """
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
