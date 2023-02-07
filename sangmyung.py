input_startdate = input("언제까지의 데이터를 보시겠습니까? (ex. 2023-02-07)")


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


while(True):
    driver = webdriver.Chrome("C:/Users/김근영/chromedriver_win32.zip/chromedriver.exe")

#driver.get("https://lib.smu.ac.kr/")

# while(True):
#     input_campus = input("어느 캠퍼스에 검색하겠습니까?(서울 / 천안) : ")
#     #input_campus = str(input_campus)
#     if((input_campus != "서울") and (input_campus != "천안")):
#         print("다시 입력해주세요")
#         continue
#     else:
#         print(input_campus + "캠퍼스에서 검색합니다.")
#         # if(input_campus == "서울"):
#         #     input_title = input("도서명을 입력하세요 : ")
#         #     driver.get("https://lib.smu.ac.kr/")
#         #     driver.find_element(By.CSS_SELECTOR, "#q")




#input_enddate = input("언제까지의 데이터를 보시겠습니까? (ex. 2023-02-07)")

#time.sleep(2)

#mainWrap > div.sponge-page-guide > form


# date = requests.get(i,headers=headers)
# news_html = BeautifulSoup(news.text,"html.parser")
# # 뉴스 제목 가져오기
# title = news_html.select_one("#ct > div.media_end_head.go_trans > div.media_end_head_title > h2")
# if title == None:
#     title = news_html.select_one("#content > div.end_ct > div > h2")

# try:
#     start_date = news_html.select_one("div#ct> div.media_end_head.go_trans > div.media_end_head_info.nv_notrans > div.media_end_head_info_datestamp > div > span")
#     news_date = html_date.attrs['data-date-time']
# except AttributeError:
#     news_date = news_html.select_one("#content > div.end_ct > div > div.article_info > span > em")
#     news_date = re.sub(pattern=pattern1,repl='',string=str(news_date))
# # 날짜 가져오기
# news_dates.append(news_date)



#driver.get("https://libnt.smuc.ac.kr/Search/BestBook50?stdate=2018-01-01&eddate=2023-02-07&strclass=")

#stdate


    driver.get("https://libnt.smuc.ac.kr/Search/BestBook50?stdate=&eddate=&strclass=")