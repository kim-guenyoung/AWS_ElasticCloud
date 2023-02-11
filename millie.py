
id = input("아이디를 입력하세요 : ")
pw = input("비밀번호를 입력하세요 : ")


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import os
import pandas as pd
import sys
from urllib.request import urlopen
import time
from selenium.webdriver.common.by import By
import requests
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import xlwt
import math

driver = webdriver.Chrome("C:/Users/김근영/chromedriver_win32.zip/chromedriver.exe")

# 칼럼 리스트 준비
book_list = []

# 밀리의 서재 베스트셀러 웹페이지를 가져옵니다.
driver.get("https://www.millie.co.kr/v3/login")
time.sleep(0.5)
driver.find_element(By.CSS_SELECTOR, '#input-14').send_keys(id)
time.sleep(0.5)
driver.find_element(By.CSS_SELECTOR, '#input-15').send_keys(pw)
driver.find_element(By.CSS_SELECTOR, "#wrap > section > div > div.login-content > div.button-area.mt16 > button").click()

time.sleep(3)

driver.find_element(By.CSS_SELECTOR, "#wrap > div > div > header > nav > ul > li:nth-child(3) > a").click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "#wrap > section > section > div.search-body > section.shortcuts > div > a.best-link.gtm-search-direct-best").click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "#wrap > section > div > section > article:nth-child(1) > h2").click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "#wrap > section > div > section > article > div > div > button:nth-child(2)").click()
time.sleep(1)
soup = BeautifulSoup(driver.page_source, 'html.parser')
books = soup.select('div.metadata')

for book in books:
    title = book.select('p.title')[0].text
    rank = book.select('p.rank')[0].text
    author = book.select('p.author')[0].text
    print(rank, title, author)
    book_list.append([rank, title, author])
df = pd.DataFrame(book_list, columns = ["순위", "제목", "저자"])


df.to_csv("밀리의 서재 " + '.csv', index = False, encoding = "utf-8-sig")
df.to_excel("밀리의 서재" + '.xls', index = False, encoding = "utf-8-sig")