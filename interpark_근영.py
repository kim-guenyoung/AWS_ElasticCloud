from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import os
import pandas as pd
from urllib.request import urlopen
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C:/Users/김근영/chromedriver_win32.zip/chromedriver.exe")

#driver = webdriver.Chrome(ChromeDriverManager().install())


# 인터파크 베스트셀러 웹페이지를 가져옵니다.
driver.get("http://book.interpark.com/display/collectlist.do?_method=BestsellerHourNew201605&bestTp=1&dispNo=028#")
time.sleep(2)

driver.find_element(By.CSS_SELECTOR, "#cateTabId2 > a > span").click() #일단은 주간으로 함.
time.sleep(2)
bsObject = BeautifulSoup(driver.page_source, 'html.parser')














# #칼럼 리스트 준비
# title = []
# author = []

# # 책의 상세 웹페이지 주소를 추출하여 리스트에 저장합니다.
# while(True):
#     book_list = bsObject.find('div', class_ = "rankBestContentList").find('ol').find_all('li')

#     for li in book_list:
#         title = li.find('div', class_ = "listItem singleType").find('div', class_ = "itemName").text
        