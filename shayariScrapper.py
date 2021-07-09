import  json
import requests
import pandas as pd
from bs4 import BeautifulSoup
# crawl to page with requests
url = "'https://www.digitalalia.in/2020/01/motivational-shayari-hindi.html"
r = requests.get(url)

# parse the output with html parser
soup = BeautifulSoup(r.text, 'html.parser')

#filter all the required attributes
quotes = soup.find_all('blockquote', attrs={'class': 'tr_bq'})

#get the length
print('Total Number of Cards Found:', len(quotes) )

count = 1

#array to store the quotes
hindiQuotes = []

#debug for the length and print the output
for post in quotes:
    #initializing a dictionary
    quotes_data = {}

    # creating a data dictionary
    quotes_data['quoteText'] = post.text.replace('\n', '')
    quotes_data['quoteAuthor'] = "आज का सुविचार"
    hindiQuotes.append(quotes_data)

# create a data frame for the list of dictionaries 
dataFrame = pd.DataFrame(hindiQuotes)

print(dataFrame)
# save to json file
dataFrame.to_json("hindiQuotes.json", orient="records", force_ascii = False)
