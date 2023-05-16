import requests
from selenium import webdriver

def world_learn (num):
    # num 길이의 리스트 생성 (초기값 0)
    eng=[0 for i in range (num)]
    kor=[0 for i in range (num)]
    mean=[0 for i in range (num)]
    
    for i in range (num):
        eng[i]=driver.find_by_element_by_xpath(f"//*[@id='tab_set_all']/div[2]/div[{i}]/div[4]/div[1]/div[1]/div/div").text
        driver.find_by_css_selector("#tab_set_all > div.card-list-title > div > div:nth-child(1) > a").click
        kor[i]=driver.find_by_element_by_xpath(f"//*[@id='tab_set_all']/div[2]/div[{i}]/div[4]/div[2]/div[1]/div/div").text
        mean=dict(zip(kor,eng))
        
