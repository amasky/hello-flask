from myapp import app
from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def _hello(name=None):
    return render_template('hello.html', name=name)
