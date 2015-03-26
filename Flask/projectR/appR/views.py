from appR import app
from flask import render_template, request
from appR.api import testapi, recipe

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/test')
@app.route('/testing')
def test():
    return "Hello, Testing World!"

@app.route('/template')
def withTemp():
    test = dict(name='test', path = 'test',  children=[])
    return render_template('test.html', test=test)

@app.route('/api', methods=['GET','POST'])
def api():
    return testapi.test_function(request)

@app.route('/curl', methods=['GET','POST'])
def curl():
    print request
    print request.args

    if request.args['url']:
        targetUrl =  request.args['url']
    else:
        targetUrl =  'http://ypark.org'
##    return testapi.curl_test('http://food2fork.com/api/search?key=f99ea1cf8741d9c23ee1b3a63542fd96&q=shredded%20chicken')
    return testapi.curl_test(targetUrl)

@app.route('/recipe', methods=['GET','POST'])
def food2fork():
    print request.args
    if 'id' in request.args and request.args['id']:
        targetUrl =  'http://food2fork.com/api/get?key=f99ea1cf8741d9c23ee1b3a63542fd96&rId='+request.args['id']
    else:
        targetUrl = 'http://food2fork.com/api/search?key=f99ea1cf8741d9c23ee1b3a63542fd96&q=shredded%20chicken'
    print targetUrl
    return recipe.get_recipe(targetUrl)

@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404