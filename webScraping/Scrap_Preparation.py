import requests
from bs4 import BeautifulSoup

page =  requests.get("https://quotes.toscrape.com/")

#Verified before printing content
if page.status_code == 200:
    parsedPAge = BeautifulSoup(page.content, 'lxml')

    #We're going to print only the content of tags
print(parsedPAge)    
print(parsedPAge)    
