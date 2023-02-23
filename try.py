from bs4 import BeautifulSoup
import requests

abc="https://www.thenakedscientists.com/articles/science-news/physics"
req = requests.get(abc)
soup = BeautifulSoup(req.text , "html.parser")
#print(soup.prettify)
#x= soup.find_all( class_="panel-pane pane-views-panes pane-featured-podcast-panel-pane-8")
x= soup.find("a")
y= soup.a.prettify

#print(x)

for link in soup.find_all('a'):
    print(link.get('href'))

#print(req.content)


"""

Transporting links to json to javascript:

import json
import sys

sys.stdout = open('links.js', 'w')

jsonobj = json.dumps(l)

print("Links = '{}'".format(jsonobj))
"""