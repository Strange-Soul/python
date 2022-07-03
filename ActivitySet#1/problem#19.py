import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import requests
import re
#url=input("Enter the Location :")
url="http://py4e-data.dr-chuck.net/comments_1545938.xml"
html=requests.get(url).content
soup=BeautifulSoup(html,'html.parser')
#print(soup.prettify())

#tree=ET.fromstring(soup)
#print(tree)
number=soup('count')
num=re.findall('\d+', number)
for n in num:
    print(n)