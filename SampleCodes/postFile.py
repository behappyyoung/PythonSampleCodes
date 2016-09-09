from sys import argv
import requests

script, filename = argv

r = requests.post('http://httpbin.org/post', files={filename: open(filename, 'rb')})
print(r, r.text)
