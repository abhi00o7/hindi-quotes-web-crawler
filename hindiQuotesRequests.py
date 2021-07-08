import json
import urllib.request
import requests
from bs4 import BeautifulSoup

# hindi quotes website आज का सुविचार
r = requests.get('https://aajkasuvichar.com/aaj-ka-suvichar/')
# content = urllib.request.urlopen('https://aajkasuvichar.com/aaj-ka-suvichar/')
# content = urllib.request.urlopen('https://www.hindishayari.biz/2019/11/motivation-shayari-in-hindi-suvichar-in.html')
content = urllib.request.urlopen('https://api.github.com/events')
# r = requests.get('https://api.github.com/events')

read_content = content.read()

soup = BeautifulSoup(read_content, 'html.parser')
print(r.status_code)
# print(r.text)
# print(read_content)
# print(soup)

