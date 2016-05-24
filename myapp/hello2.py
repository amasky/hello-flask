from myapp import app

@app.route('/hello2')
def _hello2():
    return "Hello World 2!"
