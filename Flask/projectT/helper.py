#!flask/bin/python
import os, logging
from logging.handlers import RotatingFileHandler

from appT import app

handler = RotatingFileHandler('appT/log/appT.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)
app.run(host='localhost', port=8000, debug=True)
