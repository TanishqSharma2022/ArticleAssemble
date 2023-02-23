from bs4 import BeautifulSoup
import requests

abc="https://www.thenakedscientists.com/articles/science-news/physics"
req = requests.get(abc)
soup = BeautifulSoup(req.text , "html.parser")



links = []
headlines = []
for classes in soup.find_all('h3', class_="field-content"):
    for x in classes:
        links.append("https://www.thenakedscientists.com"+x.get('href'))
        headlines.append(x.contents)

# EXTRACTING IMAGE LINKS
"""
for imgs in soup.find_all('div', class_="background-image-formatter"):
    print(imgs.get('style'))
"""


body = []



for link in links:
    scraplink = str(link)
    bodyreq = requests.get(scraplink)
    bodysoup = BeautifulSoup(bodyreq.text, "html.parser")
    ins_tag = bodysoup.ins
    ins_tag.decompose()

    for x in bodysoup.find_all('div', class_="node-body"):
        for i in x.children:
            body.append(str(i))
        
    #print(body)

#Transporting links to json to javascript:

import json
import sys

sys.stdout = open('links.js', 'w')

jsonobj = json.dumps(links)
bodyobj = json.dumps(body)

print("var Links = {}".format(jsonobj))
print("var BodyContent = {}".format(bodyobj))
