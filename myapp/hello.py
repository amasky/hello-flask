from myapp import app
from flask import render_template

@app.route('/<name>')
def _hello(name=None):
    return render_template('hello.html', name=name)
