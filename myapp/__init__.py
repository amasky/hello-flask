from flask import Flask

app = Flask(__name__)

from myapp import index
from myapp import hello
