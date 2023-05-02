import requests
from bs4 import BeautifulSoup
url="https://www.classcard.net/set/13158880/950323"

response=requests.get(url)

soup=BeautifulSoup(response.text, "html.parser")
print (soup)