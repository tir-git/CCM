#모듈 불러오기
import requests
import time
import warnings

from bs4 import BeautifulSoup
from selenium import webdriver

url="https://www.classcard.net/set/13158880/950323"

response=requests.get(url)

soup=BeautifulSoup(response.text, "html.parser")
print (soup)
