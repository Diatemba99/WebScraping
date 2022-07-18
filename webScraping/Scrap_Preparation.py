import requests
from bs4 import BeautifulSoup

page =  requests.get("https://quotes.toscrape.com/")

#Verified before printing content
if page.status_code == 200:
    parsedPAge = BeautifulSoup(page.content, 'lxml')

    #save all quotes 
    div_citations = parsedPAge.find_all('div', {'class':'quote'})

    #saving separeted values
    citation = parsedPAge.find('span', {'class':'text'})
    auteur = parsedPAge.find('small', {'class':'author'})
    tags = parsedPAge.find_all('a', {'class':'tag'})

    print(citation,auteur,tags)



    #choosing first element only
    #div_citations = parsedPAge.find_all('div', {'class':'quote'})[0]
    #print(div_citations)
    #print(div_citations)

