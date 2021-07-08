import  json
import requests
from bs4 import BeautifulSoup

r = requests.get(
    'https://www.digitalalia.in/2020/01/motivational-shayari-hindi.html')

soup = BeautifulSoup(r.text, 'html.parser')

quotes = soup.find_all('blockquote', attrs={'class': 'tr_bq'})


'''
for post in quotes:
    print (post.get_text())
'''
