
import sys
path = '/var/wwww/PythonSampleCodes/Flask/dirtree'
sys.path.insert(0, path)

if path not in sys.path:
    sys.path.append(path)

from dirtree import app
application = app


