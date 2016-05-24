from flask import Flask

app = Flask(__name__)

@app.route('/')
def _root():
    return "This is root."

from myapp import hello1
from myapp import hello2
