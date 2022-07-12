import requests
from bs4 import BeautifulSoup

page =  requests.get("https://quotes.toscrape.com/")
# print(page.content)

#to know the response code
print(page.status_code)

#Verified before printing content
if page.status_code == 200:

    #specified interpreter for showing code
    parsedPAge = BeautifulSoup(page.content, 'lxml')
    
    #print all content of html page
    print(parsedPAge)

    #print only div in html page
    print(parsedPAge.div)
else:
    print('Contenu introuvable') 









    
       