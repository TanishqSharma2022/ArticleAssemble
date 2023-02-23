from bs4 import BeautifulSoup
import requests

abc="https://www.thenakedscientists.com/articles/science-news/physics"
req = requests.get(abc)
soup = BeautifulSoup(req.text , "html.parser")



links = []

for classes in soup.find_all('h3', class_="field-content"):
    for x in classes:
        links.append("https://www.thenakedscientists.com"+x.get('href'))


#for i in links:
#    print(i)



#for link in links:
scraplink = "https://www.thenakedscientists.com/articles/science-news/smartphone-accurately-measures-blood-oxygen"
newreq = requests.get(scraplink)
soup = BeautifulSoup(newreq.text, "html.parser")

for x in soup.find_all('div', class_="node-body"):
    for i in x.children:
        print(i)    




"""

Transporting links to json to javascript:

import json
import sys

sys.stdout = open('links.js', 'w')

jsonobj = json.dumps(l)

print("Links = '{}'".format(jsonobj))
"""