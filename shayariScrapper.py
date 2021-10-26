import requests
import pandas as pd
from bs4 import BeautifulSoup


def shayariScrapper():
    # crawl to page with requests
    # url = "'https://www.digitalalia.in/2020/01/motivational-shayari-hindi.html"
    url = "https://www.digitalalia.in/2019/10/suvichar-hindi.html"

    try:
        r = requests.get(url)

        # parse the output with html parser
        soup = BeautifulSoup(r.text, 'html.parser')

        # filter all the required attributes
        # need to be changed for diffrent webpage structure.
        quotes = soup.find_all('blockquote', attrs={'class': 'tr_bq'})

        # get the length
        print('Total Number of Quote(s) Found:', len(quotes))

        # array to store the quotes
        hindiQuotes = []

        # debug for the length and print the output
        for post in quotes:
            # initializing a dictionary
            quotes_data = {}

            # creating a data dictionary
            quotes_data['quoteText'] = post.text.replace('\n', '')
            quotes_data['quoteAuthor'] = "आज का सुविचार"
            hindiQuotes.append(quotes_data)

        # create a data frame for the list of dictionaries
        dataFrame = pd.DataFrame(hindiQuotes)

        print(dataFrame)
        # save to json file
        # dataFrame.to_json("hindiMotivationalQuotes.json", orient="records", force_ascii = False)

    except SyntaxError:
        print("Syntax not defined properly!")

    except NameError:
        print("some variable(s) is(are) not defined.")

    except:
        print("An exception occurred!")

# main


if __name__ == "__main__":
    shayariScrapper()
