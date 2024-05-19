#!/usr/bin/python3
"""This script starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
    /c/<text>: display “C ” followed by the value of the text variable (replace underscores with spaces)
    /python/(<text>): display “Python ” followed by the value of the text variable (replace underscores with spaces)
        - The default value of text is “is cool”
"""
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display a simple greeting."""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display HBNB."""
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Display 'C' followed by the value of the text variable with underscores replaced by spaces."""
    return "C " + text.replace('_', ' ')

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """Display 'Python' followed by the value of the text variable with underscores replaced by spaces."""
    return "Python " + text.replace('_', ' ')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
