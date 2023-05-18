# Import Modules
import requests
import time
import warnings
import chromedriver_autoinstaller

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service

from function import world_learn

# Chrome Driver Autoinstall & Setting
print("최적의 구동 환경을 위하여 크롬 브라우저를 자동으로 설치합니다.\n이미 크롬 브라우저가 설치되어 있습니까?")
check=input("Proceed? (Y/n/a) : ")

if check=='y':
    options=webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches",["enable-logging"])
    driver=webdriver.Chrome()
    driver=webdriver.Chrome(service=Service(chromedriver_autoinstaller.install()),options=options)
else :
    print("크롬 브라우저 설치가 거부되었습니다.")
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

html=BeautifulSoup(driver.page_source, "html.parser")
cards_ele=html.find("div", class_="flip-body")
num=len(cards_ele.find_all("div", class_="flip-card"))

time.sleep(1)

# for i in range (num):
#     eng[i]=driver.find_by_element_by_xpath(f"//*[@id='tab_set_all']/div[2]/div[{i}]/div[4]/div[1]/div[1]/div/div").text
#     driver.find_by_css_selector("#tab_set_all > div.card-list-title > div > div:nth-child(1) > a").click
#     kor[i]=driver.find_by_element_by_xpath(f"//*[@id='tab_set_all']/div[2]/div[{i}]/div[4]/div[2]/div[1]/div/div").text
#     mean=dict(zip(kor,eng))
world_learn(driver,num)

print( """
원하는 기능을 선택해주세요.
1. 단어 기본학습
2. 단어 리콜학습
3. 단어 스펠학습
4. 단어 테스트
5. 전체 실행
6. 종료
""")
check=int(input("원하는 옵션을 입력해주세요. : "))

if check==1:
    print()
elif check==2:
    print()
elif check==3:
    print()
elif check==4:
    print()
elif check==5:
    print()
elif check==6:
    print("Press Ctrl+C to quit...")
    if KeyboardInterrupt:
        quit()
if ValueError:
    print()
