import requests
from bs4 import BeautifulSoup
from soupsieve import select

page =  requests.get("https://quotes.toscrape.com/")
# print(page.content)

#to know the response code
print(page.status_code)

#Verified before printing content
if page.status_code == 200:

    #specified interpreter for showing code
    parsedPAge = BeautifulSoup(page.content, 'lxml')
    
    #print all content of html page
    # print(parsedPAge)

    #print only div in html page
    # print(parsedPAge.div)

    #print only specified class in html page
    selectedClass = parsedPAge.find('li',{'class':'next'})
    #print(selectedClass)

    #print content of top 10 tags
    TopTenTags = parsedPAge.find('div',{'class':'col-md-4 tags-box'})
    # print(TopTenTags)

    #select all links on html page
    lien = parsedPAge.find_all('a')
    # print(lien)

    #select all span with class text
    citation = parsedPAge.find_all('span', {'class':'text'})
    # print(citation)

    #using only element on specified div and class
    # TopTenTagsBox = parsedPAge.find('div',{'class':'col-md-4 tags-box'})
    # TagsOnTagsBox = TopTenTagsBox.find_all('a', {'class':'tag'})
    # print(TagsOnTagsBox)

    #Doing concat of this instruction
    TopTenTagsBox = parsedPAge.find('div',{'class':'col-md-4 tags-box'}).find_all('a', {'class':'tag'})
    print(TopTenTagsBox)

else:
    print('Contenu introuvable') 










