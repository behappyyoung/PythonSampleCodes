__author__ = "young.park"
__date__ = "$Oct 8, 2015 10:09:13 AM$"

if __name__ == "__main__":
    print "testapi"
    
import pycurl
from StringIO import StringIO
from flask import render_template

def test_function(request):
    returnval = 'args == <br />' +  str(request.args)
    returnval +=  ' <br /> request ========<br />' + str(request.__dict__)
    returnval += '<br /> args == <br />' + str(request.args.__dict__)

    return returnval


def curl_test(url):
    buffer = StringIO()
    c = pycurl.Curl()
    c.setopt(c.URL, url)
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()
    return buffer.getvalue()