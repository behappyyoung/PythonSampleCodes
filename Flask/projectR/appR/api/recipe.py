__author__ = 'young'
import pycurl
from StringIO import StringIO


def get_recipe(url):
    buffer = StringIO()
    c = pycurl.Curl()
    c.setopt(c.URL, url)
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()
    print buffer
    return buffer.getvalue()