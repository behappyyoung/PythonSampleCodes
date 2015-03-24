from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/test')
@app.route('/testing')
def test():
    return "Hello, Testing World!"
