from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import os
import pandas as pd
from urllib.request import urlopen
import time
from selenium.webdriver.common.by import By
import requests
from selenium.webdriver.common.keys import Keys
import pyperclip

driver = webdriver.Chrome("C:/Users/김근영/chromedriver_win32.zip/chromedriver.exe")

# 밀리의 서재 베스트셀러 웹페이지를 가져옵니다.

driver.implicitly_wait(3)
driver.get("https://www.millie.co.kr/v3/login")

id = driver.find_element(By.CSS_SELECTOR, "#wrap > section > div > div.login-content > div:nth-child(3) > div")
id.click() #일단은 주간으로 함.
pyperclip.copy('01023043165')
id.send_keys(Keys.CONTROL, 'v')

driver.find_element(By.CSS_SELECTOR, '#wrap > section > div > div.login-content > div:nth-child(4) > div > label > div > div').click()
pyperclip.copy('0527rla!')
id.send_keys(Keys.CONTROL, 'v')
driver.find_element(By.CSS_SELECTOR, "#wrap > section > div > div.login-content > div.button-area.mt16 > button").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "#wrap > div > div > header > nav > ul > li.on")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "#wrap > section > section > div.search-body > section.shortcuts > div > a.best-link.gtm-search-direct-best")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "#wrap > section > div > section > article:nth-child(1) > div.sort-list > button:nth-child(2)")

soup = BeautifulSoup(driver.page_source, 'html.parser')
books = soup.select('div.metaData')

for book in books:
    rank = book.select('p.title')[0].text
    print(rank)