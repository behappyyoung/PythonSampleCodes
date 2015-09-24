#!flask/bin/python
import os, logging
from logging.handlers import RotatingFileHandler

from appR import app

handler = RotatingFileHandler('projectR.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)
app.run(host='192.168.10.115', port=5000, debug=True)