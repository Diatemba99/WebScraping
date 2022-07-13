import requests
from bs4 import BeautifulSoup

page =  requests.get("https://quotes.toscrape.com/")

#Verified before printing content
if page.status_code == 200:
    parsedPAge = BeautifulSoup(page.content, 'lxml')
    #print(parsedPAge.select("h1 a"))
    
    #print class
    # print(parsedPAge.select(".tag"))

    #print specified attribut
    print(parsedPAge.select("a[href='/tag/inspirational/page/1/']"))
else:
    print('Contenu introuvable')      