# Import Modules
import requests
import time
import warnings
import chromedriver_autoinstaller


from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service

from function import world_learn

# Chrome Driver Autoinstall & Setting
print("크롬 브라우저가 컴퓨터에 설치되어 있습니까?")
check=input("Proceed? (Y/n)...")

if check=='y':
    pass
else :
    print("크롬 브라우저를 설치하시겠습니까?")
    check=input("Proceed? (Y/n)...")
    if check=='y':
        options=webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches",["enable-logging"])
        driver=webdriver.Chrome()
        driver=webdriver.Chrome(service=Service(chromedriver_autoinstaller.install()),options=options)
    else :
        quit()

# Classcard Login
driver.get("https://www.classcard.net/login")
print("\n사용자의 개인정보는 프로그램에 저장되지 않으며, 로그인 용도로만 사용됩니다.\n직접 브라우저에서 로그인 할 시 오류가 발생할 수 있습니다.\n")
cc_id=input("클래스카드 ID를 입력하세요. : ")
cc_pw=input("클래스카드 비밀번호를 입력하세요. : ")
wait=WebDriverWait(driver, 10)
tag_id=wait.until(EC.visibility_of_element_located((By.ID, "login_id")))
tag_pwd=wait.until(EC.visibility_of_element_located((By.ID, "login_pwd")))
tag_id.clear()
tag_id.send_keys(cc_id)
tag_pwd.send_keys(cc_pw)
wait=WebDriverWait(driver, 10)
loginbutton=wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#loginForm > div.checkbox.primary.text-primary.text-center.m-t-md > button")))
loginbutton.click()

# Input Classcard URL 
ccsite=input("\n자동 학습을 원하는 Classcard 사이트의 URL을 입력하세요. : ")

# Check if the URL is valid
try:
    time.sleep(1)
    driver.get(ccsite)
    driver.find_element(By.XPATH, "//div[@class='p-b-sm']")
    time.sleep(1)
except:
    print("\n입력한 URL이 잘못되었습니다.\n")
    print("Press any key to quit...")
    quit()

# Classcard Vocabulary Set change range to all
wait=WebDriverWait(driver, 10)
rangesel=wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div.mw-1080 > div.p-b-sm > div.set-body.m-t-25.m-b-lg > div.m-b-md > div > a")))
rangesel.click()
rangesel1=wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div.mw-1080 > div.p-b-sm > div.set-body.m-t-25.m-b-lg > div.m-b-md > div > ul > li:nth-child(1)")))
rangesel1.click()

# Load the vocabulary set
# response=requests.get(ccsite)
# html_content=response.text
# html=BeautifulSoup(html_content, "html.parser")
# # card_element=""
# card_element=wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div.mw-1080 > div.p-b-sm > div.set-body.m-t-25.m-b-lg > div.tab-content.m-t-sm > div.tab_set_all > div.flip-body.word-set.m-t-md.m-b-mb")))
# card_element="body > div.mw-1080 > div.p-b-sm > div.set-body.m-t-25.m-b-lg > div.tab-content.m-t-sm > div.tab_set_all > div.flip-body.word-set.m-t-md.m-b-mb"

# div_elements=html.select(card_element)
# num=len(div_elements)
# print (num)

num=int(input("input num. 임시입니다"))
world_learn(ccsite,num)

time.sleep(1)

from function import eng, kor, mean
print (eng)
print(kor)
print(mean)