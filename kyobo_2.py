from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import os
import pandas as pd
from urllib.request import urlopen
import time
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(ChromeDriverManager().install())


# 교보문고의 베스트셀러 웹페이지를 가져옵니다.
driver.get("https://product.kyobobook.co.kr/bestseller/online?period=001")
bsObject = BeautifulSoup(driver.page_source, 'html.parser')

# 책의 상세 웹페이지 주소를 추출하여 리스트에 저장합니다.
book_page_urls = []
for item in bsObject.find_all('div', 'prod_info_box'):
    url = item.select('a')[0].get('href')
    book_page_urls.append(url)

# 웹페이지로부터 필요한 정보를 추출합니다. 
for index, book_page_url in enumerate(book_page_urls):
    html = urlopen(book_page_url)
    bsObject = BeautifulSoup(html, "html.parser")
    title = bsObject.find('span', 'prod_title').text
    author = bsObject.find('h3', 'title_heading').a.span.text
    image = bsObject.find('meta', {'property':'og:image'}).get('content')
    url = bsObject.find('meta', {'property':'og:url'}).get('content')
    price = bsObject.find('span', 'prod_info_price').span.text

    print(index+1, title, author, image, url, price)