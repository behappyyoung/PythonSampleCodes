import os
from app import app
from flask import Flask, render_template, jsonify, request
### custom defined functions
from app.api import testapi, recipe, fb


from routes import Mapper
map = Mapper()
map.redirect('/*(url)/', '/{url}',
             _redirect_code='301 Moved Permanently')

def _make_tree(path):
    tree = dict(name=os.path.basename(path), path = path,  children=[])
    try: lst = os.listdir(path)
    except OSError:
        pass #ignore errors
    else:
        for name in lst:
            fn = os.path.join(path, name)
            if os.path.isdir(fn):
                tree['children'].append(_make_tree(fn))
            else:
                tree['children'].append(dict(name=name))
    return tree


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/test')
@app.route('/testing')
def test():
    ##return "Hello, Testing World!"
    return render_template('plain.html')


@app.route('/showtree')
def showtree():
    path = os.path.dirname(os.path.abspath(__file__))

    pathtree =  _make_tree(path)
    app.logger.info("dumping path: %s", path)
    app.logger.info("dumping make_tree(path): %s", pathtree)
    return render_template('dirtree.html', tree=pathtree)

@app.route('/users')
def getUsers():
    return fb.getUsers()

@app.route('/menu')
def getMenu():
    return fb.getMenu()

@app.route('/dish')
@app.route('/dish/')
def getDish():
    return fb.getDish()

@app.route('/dish/<name>')
def dishDetail(name):
    return fb.getDishDetail(name)

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
    print 'targetUrl' ,targetUrl
    return testapi.curl_test(targetUrl)

@app.route('/requesttest', methods=['GET','POST'])
def request_test():
    return testapi.test_function(request)

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
