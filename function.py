import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

def world_learn (driver,num):
    # num 길이의 리스트 생성 (초기값 0)
    eng=[0 for i in range (num)]
    kor=[0 for i in range (num)]
    mean=[0 for i in range (num)]
    
    for i in num:
        eng[i]=driver.find_element(By.XPATH,f"//*[@id='tab_set_all']/div[2]/div[{i}]/div[4]/div[1]/div[1]/div/div")
        driver.find_by_css_selector("#tab_set_all > div.card-list-title > div > div:nth-child(1) > a").click
        kor[i]=driver.find_element(By.XPATH,f"//*[@id='tab_set_all']/div[2]/div[{i}]/div[4]/div[2]/div[1]/div/div")
        mean=dict(zip(kor,eng))