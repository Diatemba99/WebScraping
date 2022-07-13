import requests
from bs4 import BeautifulSoup

page =  requests.get("https://quotes.toscrape.com/")

#Verified before printing content
if page.status_code == 200:
    parsedPAge = BeautifulSoup(page.content, 'lxml')

    #using only element on specified div and class
    citations = parsedPAge.find_all('span', {'class':'text'})
    #listeCitations = []
    
    #loop for addind quotes on list
    # for cit in citations:
    #     listeCitations.append(cit.string)
    # print(listeCitations)    
    
    # print('=============================')
    # val = len(listeCitations)
    # for i in range(val):
    #     print(listeCitations[i])
    
    
    print('===========>     LISTE COMPREHENSION    <============')
    listeCitations = [citation.string for citation in citations]
    print(listeCitations)

else:
    print('Contenu introuvable')     