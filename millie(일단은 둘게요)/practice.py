import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
import sys
import os
import math
import time
from datetime import datetime
import xlwt


driver = webdriver.Chrome(os.getcwd() + "/chromedriver.exe")
url = 'https://movie.naver.com'
driver.get(url)


# 평점
# driver.find_element('By.XPATH', '//*[@id="movieEndTabMenu"]/li[5]/a').click()
# time.sleep(1)

# 칼럼 리스트 준비
score = []
text = []
user = []
date = []
good = []
bad = []

# iframe 이동
# driver.switch_to.default_content()
# driver.switch_to.frame('pointAfterListIframe')

# 전체 소스 가져오기
full_html = driver.page_source
soup = BeautifulSoup(full_html, 'html.parser')




while(True):

    # 리뷰 리스트 가져오기
    content_list =  soup.find('div',class_='ifr_area basic_ifr').find('div', class_ = 'score_result').find('ul').find_all('li')

    for li in content_list:

        # 각 요소 가져오기
        tmp_score = li.find('div', class_='star_score').find('em').text 