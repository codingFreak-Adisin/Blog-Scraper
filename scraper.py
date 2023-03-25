import requests
from bs4 import BeautifulSoup as bs
import re
import time
from csv import writer

url = "https://medium.com/"
res = requests.get(url)

# print(res.text)

soup = bs(res.text, "html.parser")
news_article = soup.find("section", {"class": "pw-homefeed"})

articles = set( map( lambda x:x.get('href'), news_article.find_all("a",attrs={"href": re.compile("^https://")})))

# print(len(articles))
#for article in articles:
#    res = requests.get(article.get("href"))
#    soup = bs(res.text, "html.parser")
#    title = (soup.find("h1",{"class": "pw-post-title"}).text if soup.find_next("h1", {"class": "pw-post-title"}) else "")
#    descs = list(map(lambda x:x.text, soup.find_all("p", {"class" : "pw-post-body-paragraph"})))
#    author = soup.find("div", {"class": "pw-author"})
#    print(f"\n\n{author}\n{title}\n{len(descs)}\n\n")

with open('data.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Url','Title', 'Description Length', 'Author']
    thewriter.writerow(header)


    for article in articles:
        url = article
        print(url)
        res = requests.get(article)
        soup = bs(res.text, "html.parser")
        title = (soup.find("h1",{"class": "pw-post-title"}).text if soup.find("h1",{"class": "pw-post-title"}) else "" )
        descs = list(map(lambda x:x.text,soup.find_all("p",{"class":"pw-post-body-paragraph"})))
        author = (soup.find("div",{"class":"pw-author"}).text if soup.find("div",{"class": "pw-author"}) else "" )

        if author and title and descs:
            info = [ url,title, descs, author]
            thewriter.writerow(info)

# To print the data in the terminal
#    if author and title and descs:
#        print(f"\n\nAuthor : {author}\nTitle: {title}\nDesc len :{len(descs)}\n\n") 
#    time.sleep(2)


