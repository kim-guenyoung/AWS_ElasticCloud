import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
import sys
import os
import math
import time
from datetime import datetime
import xlwt

driver = webdriver.Chrome("C:/Users/김근영/chromedriver_win32.zip/chromedriver.exe")
driver.get("https://libnt.smuc.ac.kr/Search/BestBook50?stdate=&eddate=&strclass=")


#칼럼 리스트 준비
title = []
author = []

#iframe 이동
#driver.switch_to.default_content()
#driver.switch_to.frame('pointAfterListFrame')

#전체 소스 가져오기
full_html = driver.page_source
soup = BeautifulSoup(full_html, 'html.parser')

while(True):
    #베스트셀러 목록 가져오기
    # content_list =  soup.find('div',class_='ifr_area basic_ifr').find('div', class_ = 'score_result').find('ul').find_all('li')
    # tmp_text = li.find('div', class_='score_reple').find('p').text

    #best_seller = soup.find('div', class_ = 'book-title-page').find('dl', class_ = 'row').find_all('dd', class_ = 'col-md-8')
    best_seller = soup.find('div', class_ = 'book-title-page').find_all('dl', class_ = 'row')
    #find_all('dd', class_ = 'col-md-8')
    
    for dl in best_seller:
        #각 요소 가져오기
        tmp_title = dl.soup.find('dd', class_ = 'col-md-8').find_all('strong').text
        #tmp_author = dl.find('dd', class_ = 'col-md-8').find('br').text
        #tmp_score = dl.find('strong').find('a').text
        #title = dl.find('col-md-8').text