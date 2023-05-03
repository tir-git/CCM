# Import Modules
import requests
import time
import warnings
import chromedriver_autoinstaller

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service

# Chrome Driver Autoinstall & Setting
options=webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches",["enable-logging"])
driver=webdriver.Chrome(service=Service(chromedriver_autoinstaller.install()),options=options)

# Classcard URL 입력받기
ccsite=input("자동 학습을 원하는 Classcard 사이트의 URL을 입력하세요. : ")

print(ccsite)
