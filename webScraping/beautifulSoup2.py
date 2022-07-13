import requests
from bs4 import BeautifulSoup

page =  requests.get("https://quotes.toscrape.com/")

#Verified before printing content
if page.status_code == 200:

    #specified interpreter for showing code
    parsedPAge = BeautifulSoup(page.content, 'lxml')

    #using only element on specified div and class
    TopTenTagsBox = parsedPAge.find('div',{'class':'col-md-4 tags-box'})
    TagsOnTagsBox = TopTenTagsBox.find_all('a', {'class':'tag'})
    # print(TagsOnTagsBox)

    #listing content on tags
    #for tag in TagsOnTagsBox:
        # print(tag.string)

    #listing attributes on tags
    for tag in TagsOnTagsBox:
        print(tag.attrs)

    #listing one element of attribut on tags
    print('================================')
    for tag in TagsOnTagsBox:
        print(tag.attrs['href'])  

    #Sometimes string method doesn't work properly so we use get_text() 
    print('================================')
    print(parsedPAge.h1.get_text())         

else:
    print('Contenu introuvable') 










