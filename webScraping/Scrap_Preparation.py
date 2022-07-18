import requests
import json
from bs4 import BeautifulSoup


page =  requests.get("https://quotes.toscrape.com/")

#Verified before printing content
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

#save content in list
list_citations = []
for citation in div_citations:
    list_citations.append(extract_data(citation))
#print(list_citations)


#saving data in json file
with open('e:\COURSES\CODES\WEBSCRAPING\EXO\webScraping\quotes.json', 'w') as f:
    json.dump(list_citations, f)




"""
============================================================
============================================================
============================================================
"""
""" citation = div_citations.find('span', {'class':'text'}).get_text()
    auteur = div_citations.find('small', {'class':'author'}).get_text()
    #create list comprehension for saving tags on list
    tags =[tag.get_text() for tag in div_citations.find_all('a', {'class':'tag'})]
    

    #tags = div_citations.find_all('a', {'class':'tag'})
    #print(citation,auteur,tags)
    #create dictionary
    data = {
        'citation' : citation,
        'auteur' : auteur,
        'tags' : tags
    }
    print(data)



    #choosing first element only
    #div_citations = parsedPAge.find_all('div', {'class':'quote'})[0]
    #print(div_citations)
    #print(div_citations)
"""