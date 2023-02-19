# 여행		

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

# 칼럼 리스트 준비
book_list = []
rank = 0
# 밀리의 서재 베스트셀러 웹페이지를 가져옵니다.(여기까지 로그인)

for i in range(1, 3):
    
    driver.get("https://www.aladin.co.kr/shop/common/wbest.aspx?BestType=EBookBestseller&BranchType=9&CID=38408&page="+str(i)+"&cnt=300&SortOrder=1")
    time.sleep(0.5)
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # 1위 책 클릭(대여 횟수 긁어오기 위함)
    books = soup.select('div.ss_book_box')
    for book in books:
        try:
            rank += 1
            title = book.select('a.bo3')[0].text

            
            li_tags = book.find_all('li')
            second_li_tag = li_tags[2] # 2. 두 번째 li 태그 선택
            info = second_li_tag.get_text() # 3. 두 번째 li 태그 내부의 첫 번째 내용 가져오기

            author=info.split('|')[0]
            publisher=info.split('|')[1]
            date=info.split('|')[2] 


            stars=book.select_one("div.ss_book_list img")
        
            star=0
            
            if stars==None:
                
                star=0
                
            elif stars['src']=="//image.aladin.co.kr/img/common/star_s10.gif":
                
                star=5
                
            elif stars['src']=="//image.aladin.co.kr/img/common/star_s9.gif":
                
                star=4.5
                
            elif stars['src']=="//image.aladin.co.kr/img/common/star_s8.gif":
                
                star=4
                
            elif stars['src']=="//image.aladin.co.kr/img/common/star_s7.gif":
                
                star=3.5
                
            elif stars['src']==f"//image.aladin.co.kr/img/common/star_s6.gif":
                
                star=3
                
            elif stars['src']==f"//image.aladin.co.kr/img/common/star_s5.gif":
                
                star=2.5

            elif stars['src']==f"//image.aladin.co.kr/img/common/star_s4.gif":
                
                star=2

            print(rank, title, author, publisher, date, star)
            book_list.append([rank, title, author, publisher, date, star])
            i += 1
        
        except IndexError:
            pass
                
            
df = pd.DataFrame(book_list, columns = ["순위", "제목", "저자", "출판사", "출간일", "별점"])


df.to_csv("알라딘_여행" + '.csv', index = False, encoding = 'utf-8-sig')
# # df.to_excel("알라딘_여행" + '.xls', index = False, encoding = "utf-8-sig")

print(df)