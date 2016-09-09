from bs4 import BeautifulSoup
import requests

url = 'https://stanfordhealthcare.org'

# using requests
try:
    response = requests.get(url)
    message = response.content
    soup = BeautifulSoup(message, 'html.parser')
    mydiv = str(soup.find("div", class_="stanford-now-pulse"))
    file_ = open('pulseDiv', 'w')
    file_.write(mydiv)
    file_.close()
except requests.exceptions.RequestException as e:  # This is the correct syntax
    print (e)
    message = "could not fetch %s" % url
    print (message)
    file_ = open('pulseDiv', 'r')
    mydiv = file_.read()
    file_.close()

print(mydiv)

