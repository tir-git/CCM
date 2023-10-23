# Import Modules
# import requests
import time
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import chromedriver_autoinstaller

from bs4 import BeautifulSoup
import requests

import function

# Start
print("""
CCM: ClassCard Macro by tir-tir
version: 1.0.0
""")

# Chrome Driver Autoinstall & Setting
print("구동을 위해 크롬 드라이버를 설치하는 중입니다...")
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches",["enable-logging"])
chromedriver_autoinstaller.install()
driver = webdriver.Chrome(options=options)

# Classcard Login
driver.get("https://www.classcard.net/login")
print("\n사용자의 개인정보는 프로그램에 저장되지 않으며, 로그인 용도로만 사용됩니다.\n직접 브라우저에서 로그인 할 시 오류가 발생할 수 있습니다.\n")
cc_id = input("클래스카드 ID를 입력하세요. : ")
cc_pw = input("클래스카드 비밀번호를 입력하세요. : ")
wait = WebDriverWait(driver, 10)
tag_id = wait.until(EC.visibility_of_element_located((By.ID, "login_id")))
tag_pwd = wait.until(EC.visibility_of_element_located((By.ID, "login_pwd")))
tag_id.clear()
tag_id.send_keys(cc_id)
tag_pwd.send_keys(cc_pw)
wait = WebDriverWait(driver, 10)
loginbutton = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#loginForm > div.checkbox.primary.text-primary.text-center.m-t-md > button")))
loginbutton.click()

# Input Classcard URL 
ccsite = input("\n자동 학습을 원하는 Classcard 사이트의 URL을 입력하세요. : ")


# Check if the URL is valid
try:
    time.sleep(1)
    driver.get(ccsite)
    driver.find_element(By.XPATH, "//div[@class='mw-1080']")
    time.sleep(1)
except:
    print("\n입력한 URL이 잘못되었습니다.\n")
    print("Press any key to quit...")
    quit()

# Classcard Vocabulary Set change range to all
wait = WebDriverWait(driver, 10)
rangesel = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div.mw-1080 > div.p-b-sm > div.set-body.m-t-25.m-b-lg > div.m-b-md > div > a")))
rangesel.click()

rangesel1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div.mw-1080 > div.p-b-sm > div.set-body.m-t-25.m-b-lg > div.m-b-md > div > ul > li:nth-child(1)")))
rangesel1.click()

print("asdf")

response = requests.get(ccsite)
soup = BeautifulSoup(response.text, 'html.parser')
print("asdf")
# elements = soup.select('.mw-1080 .p-b-sm .set-body .m-t-25 .m-b-lg .tab-content .m-t-sm .tap-pane .fade .active .in .flip-body .word-set .m-t-md .m-b-md .flip-card .done')
elements = soup.select('.mw-1080 .p-b-sm')
print("asdf")
print(elements)
# for factors in elements:
#     data_idx = factors.get('data-idx')
#     print(f"data-idx: {data_idx}")


