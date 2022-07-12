from ast import If
import requests

page =  requests.get("https://github.com/Diatemba99/")
print(page)
# print(page.content)

#to know the response code
print(page.status_code)

#Verified before printing content
if page.status_code == 200:
    print(page.content)
else:
    print('Contenu introuvable')    