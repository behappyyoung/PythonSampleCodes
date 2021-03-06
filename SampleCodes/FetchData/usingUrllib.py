import urllib2, sys

script, url = sys.argv

# using urllib2

if int(sys.version[4:6]) >= 9:  # for python 2.7.9 above..
    newversion = True
    import ssl

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
else:
    newversion = False

try:
    if newversion:  # for python 2.7.9 above..
        message = urllib2.urlopen(url, context=ctx).read()
    else:
        message = urllib2.urlopen(url).read()
except urllib2.URLError as e:
    print(e)
    message = "could not fetch %s" % url


print(message)