from myapp import app

@app.route('/hello1')
def _hello1():
    return "Hello World 1!"
