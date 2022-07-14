from re import A
import requests
from bs4 import BeautifulSoup

page =  requests.get("https://quotes.toscrape.com/")

#Verified before printing content
if page.status_code == 200:
    parsedPAge = BeautifulSoup(page.content, 'lxml')

    #Scap using subling 
    sibling_s = BeautifulSoup("<a> <b>text1</b> <c>text2</c> </a>", 'lxml')
    #Find the first quote
    FirstQuote = parsedPAge.find('div', {'class':'quote'})
    
    #print only tags of FirstQuote
    # print(FirstQuote.contents)
    # print("="*45)
    #Using contents create list & we're going to print specified element
    # print(FirstQuote.contents[5])

    #Know parent tag
    #print(FirstQuote.parent)

    #PRINTING ONLY ATTRIBUTES OF PARENT TAG
    #print(FirstQuote.parent.attrs)

    #Scap using subling 
    sibling_s = BeautifulSoup("<a><b>text1</b><c>text2</c></a>", 'lxml')
    print(sibling_s.b.next_sibling)
    print(sibling_s.c.previous_sibling)
    


