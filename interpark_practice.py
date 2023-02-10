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

#driver = webdriver.Chrome(ChromeDriverManager().install())


# 인터파크 베스트셀러 웹페이지를 가져옵니다.

url = "http://book.interpark.com/display/collectlist.do?_method=BestsellerHourNew201605&bestTp=1&dispNo=028#"
response = driver.get(url)

# driver.get("http://book.interpark.com/display/collectlist.do?_method=BestsellerHourNew201605&bestTp=1&dispNo=028#")
# time.sleep(2)


# driver.find_element(By.CSS_SELECTOR, "#cateTabId2 > a > span").click() #일단은 주간으로 함.
# time.sleep(2)
# bsObject = BeautifulSoup(driver.page_source, 'html.parser')


response = requests.get(url)
dom = BeautifulSoup(response.text, "html.parser")
type(dom)


elements = dom.select("#content > div.rankBestWrapper > div.rankBestContainer > div.rankBestContents > div > div.rankBestContentList > ol > li:nth-child(1)")
items = []
for element in elements:
    data = {
        "title" : element.select_one("div.itemName > strong").text
    }

best_interpark = pd.DataFrame(items)
best_interpark.to_csv('./best_interpark.csv', index = False)
print(best_interpark)