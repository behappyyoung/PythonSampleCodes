import os, logging
from logging.handlers import RotatingFileHandler
from flask import Flask, render_template, jsonify

app = Flask(__name__)

def make_tree(path):
    tree = dict(name=os.path.basename(path), children=[])
    try: lst = os.listdir(path)
    except OSError:
        pass #ignore errors
    else:
        for name in lst:
            fn = os.path.join(path, name)
            if os.path.isdir(fn):
                tree['children'].append(make_tree(fn))
            else:
                tree['children'].append(dict(name=name))
    return tree

@app.route('/')
def dirtree():
##    path = os.path.expanduser(u'~')
    path ='/var/www/PythonSampleCodes/Flask/dirtree'

    pathtree =  make_tree(path)
    app.logger.info("dumping path: %s", path)
    app.logger.info("dumping make_tree(path): %s", pathtree)
##    return jsonify(**pathtree)
    return render_template('dirtree.html', tree=pathtree)

if __name__=="__main__":
    handler = RotatingFileHandler('flask.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.run(host='localhost', port=8888, debug=True)
