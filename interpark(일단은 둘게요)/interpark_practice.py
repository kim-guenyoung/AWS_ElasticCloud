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

driver = webdriver.Chrome("C:/Users/김근영/chromedriver_win32.zip/chromedriver.exe")

# 인터파크 베스트셀러 웹페이지를 가져옵니다.
driver.get("http://book.interpark.com/display/collectlist.do?_method=BestsellerHourNew201605&bestTp=1&dispNo=028#")
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, "#cateTabId2 > a > span").click() #일단은 주간으로 함.
time.sleep(1)
soup = BeautifulSoup(driver.page_source, 'html.parser')
books = soup.select('div.itemName')

for book in books:
    rank = book.select('strong')[0].text
    print(rank)