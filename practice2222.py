import requests
from bs4 import BeautifulSoup
import csv

# 알라딘 주간 베스트 100권 크롤링
# 2/2 ~ 2/8 1주 기준

# 책 정보 추출 함수
def extract_book(html):  
    subject=html.select_one("div.ss_book_list a.bo3").text
    
    info=html.select("div.ss_book_list li")[0].text
    
    if info=="ePub"or info=="PDF" or info=="무료PDF" or info=="대여ePub" or info == "ePub정가인하" or info=="정가인하":
        
        info=html.select("div.ss_book_list li")[2].text
        
    else:
        
        info=html.select("div.ss_book_list li")[3].text
        
    writer=info.split('|')[0]
    
    publisher=info.split('|')[1]
    
    date=info.split('|')[2]
    
    stars=html.select_one("div.ss_book_list img")
    
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
    
    return {
        'subject': subject,
        'writer':writer,
        'publisher':publisher,
        'date':date,
        'star':star
    }

# 각 페이지마다 책 정보 추출 함수
def extract_books(page_count):
    books = []
    
    for page in range(page_count):
    
        print(f"Scrapping page {page+1}")
        
        rs = requests.get(f"https://www.aladin.co.kr/shop/common/wbest.aspx?BestType=EBookBestseller&BranchType=9&CID=0&page={page+1}&cnt=300&SortOrder=1")
        
        soup = BeautifulSoup(rs.text, "html.parser")
        
        results=soup.find_all("div",class_="ss_book_box")
        
        for rs in results:
            
            book = extract_book(rs)
            
            books.append(book)
            
    return books

# CSV 저장
# 1-50 / 51-100 두 페이지만 진행
books=extract_books(2)

file=open("aladin_best100.csv",mode="w")

write=csv.writer(file)

write.writerow(["subject", "writer", "publisher","date", "star"])

for book in books:
    
    write.writerow(list(book.values()))

import pandas as pd

df=pd.read_csv("aladin_best100.csv",encoding='cp949')
print(df)