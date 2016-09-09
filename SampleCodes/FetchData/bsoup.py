from bs4 import BeautifulSoup
import requests, sys

script, url = sys.argv

# using requests
try:
    response = requests.get(url)
    print (response.status_code)
    message = response.content
except requests.exceptions.RequestException as e:  # This is the correct syntax
    print (e)
    message = "could not fetch %s" % url
    print (message)
    exit(1)

soup = BeautifulSoup(message, 'html.parser')
mydiv = soup.find("div", class_="stanford-now-pulse")
print(mydiv)