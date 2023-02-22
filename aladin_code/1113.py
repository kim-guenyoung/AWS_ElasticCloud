from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
from urllib.request import urlopen
import time
from selenium.webdriver.common.by import By
import requests
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import xlwt

driver = webdriver.Chrome("C:/Users/김근영/chromedriver_win32.zip/chromedriver.exe")

book_list = []
driver.get("https://www.aladin.co.kr/shop/common/wbest.aspx?BestType=EBookBestseller&BranchType=9&CID=38404&page=1&cnt=300&SortOrder=1")



soup = BeautifulSoup(driver.page_source, 'html.parser')

books = soup.select('div.ss_book_box')
def get_title(book):
    title = book.select('a.bo3')[0].text
    return title

for book in books:
    title = get_title(book)

    book_list.append(title)
print(book_list)