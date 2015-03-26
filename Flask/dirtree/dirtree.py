import os, logging
from logging.handlers import RotatingFileHandler
from flask import Flask, render_template, jsonify

app = Flask(__name__)

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
def dirtree():
    path = os.path.dirname(os.path.abspath(__file__))

    pathtree =  _make_tree(path)
    app.logger.info("dumping path: %s", path)
    app.logger.info("dumping make_tree(path): %s", pathtree)
    return render_template('dirtree.html', tree=pathtree)

if __name__=="__main__":
    handler = RotatingFileHandler('flask.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.run(host='192.168.10.115', port=8080, debug=True)
