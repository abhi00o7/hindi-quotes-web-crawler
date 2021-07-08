import json
import urllib.request
import requests
from bs4 import BeautifulSoup

# hindi quotes website आज का सुविचार
r = requests.get('https://aajkasuvichar.com/aaj-ka-suvichar/')
content = urllib.request.urlopen()
# r = requests.get('https://api.github.com/events')

# print(r.status_code)
print(r.text)

