__author__ = 'young'
import pycurl
from StringIO import StringIO

def test_function(request):
    # print request.args
    # print request.__dict__
    # print request.args.__dict__

    return 'test return'


def curl_test(url):
    buffer = StringIO()
    c = pycurl.Curl()
    c.setopt(c.URL, url)
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()
    return buffer.getvalue()