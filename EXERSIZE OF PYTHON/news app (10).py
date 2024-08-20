import requests
import json
query = input("which kind of news you want? :- ")
url = f"https://newsapi.org/v2/everything?q={query}&form=2023-01-28&sortBy=publishedAt&apikey=aefdebdbc0bf43dc841c32ca186b0f31"

r=requests.get(url)
news = json.loads(r.text)
# print(news,type(news))
for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("***************---------------******************")


