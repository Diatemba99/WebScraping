import requests
import json
import pandas as pd
from bs4 import BeautifulSoup

page =  requests.get("https://quotes.toscrape.com/")

if page.status_code == 200:
    parsedPAge = BeautifulSoup(page.content, 'lxml')
    div_citations = parsedPAge.find_all('div', {'class':'quote'})
   
    def extract_data(div_citations):
        citation = div_citations.find('span', {'class':'text'}).get_text()
        auteur = div_citations.find('small', {'class':'author'}).get_text()
        tags =[tag.get_text() for tag in div_citations.find_all('a', {'class':'tag'})]
        data = {
            'citation' : citation,
            'auteur' : auteur,
            'tags' : tags
        }
        return data

list_citations = []
for citation in div_citations:
    list_citations.append(extract_data(citation))
data_pd = pd.DataFrame.from_dict(list_citations)

data_pd.to_json('e:\COURSES\CODES\WEBSCRAPING\EXO\webScraping\citations.json')
data_pd.to_csv('e:\COURSES\CODES\WEBSCRAPING\EXO\webScraping\citations.csv')

