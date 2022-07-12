import requests

page =  requests.get("https://quotes.toscrape.com/")
print(page)
print(page.content)