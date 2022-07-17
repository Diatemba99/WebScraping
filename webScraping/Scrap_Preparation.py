import requests
from bs4 import BeautifulSoup

page =  requests.get("https://quotes.toscrape.com/")

#Verified before printing content
if page.status_code == 200:
    parsedPAge = BeautifulSoup(page.content, 'html5')

    #We're going to print only the content of tags
print(parsedPAge)    
print(parsedPAge)    
