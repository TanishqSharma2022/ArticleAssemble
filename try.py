from bs4 import BeautifulSoup
import requests

abc="https://www.thenakedscientists.com/articles/science-news/physics"
req = requests.get(abc)
soup = BeautifulSoup(req.text , "html.parser")
#print(soup.prettify)
htcon= soup.find_all(class_="col-xs-12 col-lg-4")
x= soup.find("a")
y= soup.a.prettify

#print(x)
#print(htcon.get('href'))

for link in soup.find_all("h3" , class_="field-content"):
     for i in link:

        print(i.get('href'))
    

   #lis=link.get('href')
   #print(lis)

#print(req.content)

"""
htcon=str(htcon)
openfile=open('htm.html','r+')
openfile.write(htcon)

openfile.close()
"""



