from appT import app
from flask import render_template, request

@app.route('/')
@app.route('/index')
def index():
    return "Hello, Testing World!"
    

@app.route('/test')
@app.route('/testing')
def test():
    test = dict(name='test', path = 'test',  children=[])
    return render_template('index.html', title='Home', test=test)

@app.route('/example')
def withTemp():
    test = dict(name='test', path = 'test',  children=[])
    return render_template('example.html', test=test)

@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404