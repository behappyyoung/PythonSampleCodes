from appT import app
from flask import render_template, request


@app.route('/')
@app.route('/index')
def index():
    return "Hello, appT app /index Testing World!"

@app.route('/testing')
def test_html():
    test = dict(name='test', path='test',  children=[])
    return render_template('test.html', title='Testing', test=test)


@app.route('/python')
def python():
    return render_template('python/xml.xml')


@app.route('/example')
def withTemp():
    test = dict(name='test', path = 'test',  children=[])
    return render_template('example.html', test=test)

@app.route('/generic')
def generic():
    return render_template('generic.html')

@app.route('/xml')
def xml():
    return render_template('xml.xml')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('400.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500