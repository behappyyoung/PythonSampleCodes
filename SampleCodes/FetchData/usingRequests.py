import requests, sys

script, url = sys.argv

# using requests
try:
    response = requests.get(url)
    print (response.status_code)
    message = response.content
except requests.exceptions.RequestException as e:  # This is the correct syntax
    print(e)
    message = "could not fetch %s" % url


print(message)