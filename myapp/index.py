from myapp import app
from flask import render_template

@app.route('/')
def _index():
    return render_template('index.html', message="Hello World!")
