from elasticsearch import Elasticsearch
es = Elasticsearch('https://vitaminc.kb.ap-northeast-2.aws.elastic-cloud.com:9243')
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
from urllib.request import urlopen
import urllib.request as req
import time
from selenium.webdriver.common.by import By
import requests
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import json
from collections import OrderedDict
import requests

driver = webdriver.Chrome("C:/Users/김근영/chromedriver_win32.zip/chromedriver.exe")


# 칼럼 리스트 준비
book_list = []

smu_genre_dict = { 
    3 : "가정/생활", #요리/살림
    4 : "가정/생활", #건강/취미
    5 : "경제/비즈니스", #경제/경영
#    6 : "문학", #고전
    7 : "자연/과학", #과학, 사회과
    8 : "강의지원도서", #대학교재/전문서적
#    9 : "라이트 노벨",
    10 : "문학", #소설/시/희곡
#    11 : "사전/기타",
    12 : "인문", #사회과학
#    13 : "수험서/자격증",
#    14 : "어린이",
    15 : "에세이/산문", # 에세이, 자기계발
#    16 : "여행",
#    17 : "역사",
    18 : "문화/예술", # 예술/대중문화
    19 : "외국어", #외국어
#    20 : "유아",
    21 : "인문", #인문학
#    22 : "인물/평전",
    23 : "에세이/산문",
#    24 : "잡지",
#    25 : "전집/중고전집",
#    26 : "종교/역학",
    27 : "가정/생활", #좋은부모
#    28 : "참고서/학습서",
#    29 : "청소년",
    30 : "컴퓨터/인터넷", # 컴퓨터/모바일
}

aladin_genre_dict = { 
    3 : "요리/살림",
    4 : "건강/취미",
    5 : "경제경영",
    # 6 :/ "고전",
    7 : "과학",
    8 : "대학교재/전문서적",
    # 9 : "라이트 노벨",
    10 : "소설/시/희곡",
    # 11 : "사전/기타",
    12 : "사회과학",
    # 13 : "수험서/자격증",
    # 14 : "어린이",
    15 : "에세이",
    # 16 : "여행",
    # 17 : "역사",
    18 : "예술/대중문화",
    19 : "외국어",
    # 20 : "유아",
    21 : "인문학",
    # 22 : "인물/평전",
    23 : "자기계발",
    # 24 : "잡지",
    # 25 : "전집/중고전집",
    # 26 : "종교/역학",
    27 : "좋은 부모",
    # 28 : "참고서/학습서",
    # 29 : "청소년",
    30 : "컴퓨터/모바일"
}
#title = []; author = []; publisher = []; date = []; star = []; genre= []; price= [];
df = pd.DataFrame(book_list, columns = ["순위", "제목", "알라딘_저자", "알라딘_출판사", "알라딘_출간일", "알라딘_별점", "알라딘_장르", "상명장르", "알라딘_가격"])
    
df = pd.DataFrame(book_list, columns = ["순위", "제목", "알라딘_저자", "알라딘_출판사", "알라딘_출간일", "알라딘_별점", "알라딘_장르", "상명장르", "알라딘_가격"])
driver.get("https://www.aladin.co.kr/shop/common/wbest.aspx?BestType=EBookBestseller&BranchType=9&CID=38409")
for smu_genre_num in range(3, 30):
    
    if(smu_genre_num == 3):
        smu_genre_id = 38409
        
    if(smu_genre_num == 6 or smu_genre_num == 9 or smu_genre_num == 11 or smu_genre_num == 13 or smu_genre_num == 14 or smu_genre_num == 16 or smu_genre_num == 17
    or smu_genre_num == 20 or smu_genre_num == 22 or smu_genre_num == 24 or smu_genre_num == 25 or smu_genre_num == 26 or smu_genre_num == 28
    or smu_genre_num == 29):
        smu_genre_num += 1
        continue

    elif(smu_genre_num == 4):
        smu_genre_id = 56388
    elif(smu_genre_num == 5):
        smu_genre_id = 38398
    elif(smu_genre_num == 6):
        smu_genre_id = 38414
    elif(smu_genre_num == 7):
        smu_genre_id = 38405
    elif(smu_genre_num == 8):
        smu_genre_id = 38422
    # elif(smu_genre_num == 9):
    #     smu_genre_id = 56548
    elif(smu_genre_num == 10):
        smu_genre_id = 38396
    # elif(smu_genre_num == 11):
    #     smu_genre_id = 38419
    elif(smu_genre_num == 12):
        smu_genre_id = 38404
    # elif(smu_genre_num == 13):
    #     smu_genre_id = 38412
    # elif(smu_genre_num == 14):
    #     smu_genre_id = 38406
    elif(smu_genre_num == 15):
        smu_genre_id = 56387
    # elif(smu_genre_num == 16):
    #     smu_genre_id = 38408
    # elif(smu_genre_num == 17):
    #     smu_genre_id = 38397
    elif(smu_genre_num == 18):
        smu_genre_id = 38402
    elif(smu_genre_num == 19):
        smu_genre_id = 38411
    # elif(smu_genre_num == 20):
    #     smu_genre_id = 38424
    elif(smu_genre_num == 21):
        smu_genre_id = 38403
    # elif(smu_genre_num == 22):
    #     smu_genre_id = 38399
    elif(smu_genre_num == 23):
        smu_genre_id = 38400
    # elif(smu_genre_num == 24):
    #     smu_genre_id = 38417
    # elif(smu_genre_num == 25):
    #     smu_genre_id = 38426
    # elif(smu_genre_num == 26):
    #     smu_genre_id = 38410
    elif(smu_genre_num == 27):
        smu_genre_id = 38413
    # elif(smu_genre_num == 28):
    #     smu_genre_id = 38420
    # elif(smu_genre_num == 29):
    #     smu_genre_id = 38407
        
        
    smu_genre_num += 1
    time.sleep(1)

    for i in range(1, 3):
        driver.get("https://www.aladin.co.kr/shop/common/wbest.aspx?BestType=EBookBestseller&BranchType=9&CID="+str(smu_genre_id)+"&page="+str(i)+"&cnt=300&SortOrder=1")
        
        time.sleep(0.5)

        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # 1위 책 클릭(대여 횟수 긁어오기 위함)

        books = soup.select('div.ss_book_box')        
        li_tags = book.find_all('li')
        second_li_tag = li_tags[2] # 2. 두 번째 li 태그 선택
        info = second_li_tag.get_text() # 3. 두 번째 li 태그 내부의 첫 번째 내용 가져오기
        
        def get_title(soup):
            title = soup.select('a.bo3')[0].text
            return title
        def get_rank(soup):
            rank = book.select("td")[0].text
            return rank

        def get_author(book):
            author=info.split('|')[0]
            return author

        def get_publisher(book):
            
            publisher = info.split('|')[1]
            return publisher
        def get_date(book):
            date=info.split('|')[2]
            return date

        def get_price(book):
            price = soup.find('span', {'class': 'ss_p2'}).b.find('span').text
            return price
        def get_star(book):
            stars = book.select_one("div.ss_book_list img")
            if stars is None:
                return 0
            elif stars['src'] == "//image.aladin.co.kr/img/common/star_s10.gif":
                return 5
            elif stars['src'] == "//image.aladin.co.kr/img/common/star_s9.gif":
                return 4.5
            elif stars['src'] == "//image.aladin.co.kr/img/common/star_s8.gif":
                return 4
            elif stars['src'] == "//image.aladin.co.kr/img/common/star_s7.gif":
                return 3.5
            elif stars['src'] == "//image.aladin.co.kr/img/common/star_s6.gif":
                return 3
            elif stars['src'] == "//image.aladin.co.kr/img/common/star_s5.gif":
                return 2.5
            elif stars['src'] == "//image.aladin.co.kr/img/common/star_s4.gif":
                return 2
            else:
                return 0
        
        for book in books:
            try: #일반적인 경우
                # title = book.select('a.bo3')[0].text
                # rank = book.select("td")[0].text
                
                # li_tags = book.find_all('li')
                # second_li_tag = li_tags[2] # 2. 두 번째 li 태그 선택
                # info = second_li_tag.get_text() # 3. 두 번째 li 태그 내부의 첫 번째 내용 가져오기

                # author=info.split('|')[0]
                # publisher=info.split('|')[1]
                # date=info.split('|')[2] 
                
                # price = soup.find('span', {'class': 'ss_p2'}).b.find('span').text
                def get_title(soup):
                    titles = soup.select('a.bo3')[0].text
                    return title
                def get_rank(book):
                    ranks = book.select("td")[0].text
                    return rank

                def get_author(book):
                    info = book.find('p', {'class': 'mt5'}).text
                    author = info.split('|')[0].strip()
                    return author

                def get_publisher(soup):
                    info = book.find('p', {'class': 'mt5'}).text
                    publisher = info.split('|')[1].strip()
                    return publisher
                
                def get_date(soup):
                    info = book.find('p', {'class': 'mt5'}).text
                    date=info.split('|')[2].strip()
                    return date

                def get_price(soup):
                    price = soup.find('span', {'class': 'ss_p2'}).b.find('span').text
                    return price
                
                smu_genre = smu_genre_dict[smu_genre_num - 1]
                aladin_genre = aladin_genre_dict[smu_genre_num - 1]
                title = get_title(book)
                author = get_author(book)
                publisher = get_publisher(book)
                date = get_date(book)
                star = get_star(book)
                
                i += 1
                

            except IndexError: #행사 상품
                li_tags = book.find_all('li')
                third_li_tag = li_tags[3] # 2. 두 번째 li 태그 선택
                info = third_li_tag.get_text() # 3. 두 번째 li 태그 내부의 첫 번째 내용 가져오기

                title = book.select('a.bo3')[0].text
                price = soup.find('span', {'class': 'ss_p2'}).b.find('span').text
                rank = book.select("td")[0].text
                
                star = get_star(book)
                try: #only 행사 상품
                    li_tags = book.find_all('li')
                    third_li_tag = li_tags[3] # 2. 두 번째 li 태그 선택
                    info = third_li_tag.get_text() # 3. 두 번째 li 태그 내부의 첫 번째 내용 가져오기

                    # author=info.split('|')[0]
                    # publisher=info.split('|')[1]
                    # date=info.split('|')[2]

                    def get_title(book):
                        title = soup.select('a.bo3')[0].text
                        return title
                    def get_rank(book):
                        rank = book.select("td")[0].text
                        return rank

                    def get_author(book):
                        author=info.split('|')[0]
                        return author

                    def get_publisher(book):
                        publisher = info.split('|')[1]
                        return publisher
                    def get_date(book):
                        date=info.split('|')[2]
                        return date

                    def get_price(book):
                        price = soup.find('span', {'class': 'ss_p2'}).b.find('span').text
                        return price
                    smu_genre = smu_genre_dict[smu_genre_num - 1]
                    aladin_genre = aladin_genre_dict[smu_genre_num - 1]
                    

                except IndexError: #행사 상품은 아닌데, 출판사가 없음.
                    second_li_tag = li_tags[2]
                    info = second_li_tag.get_text()
                    author=info.split('|')[0]
                    publisher=None
                    date=info.split('|')[1] 

                    def get_title(book):
                        title = soup.select('a.bo3')[0].text
                        return title

                    def get_rank(book):
                        rank = book.select("td")[0].text
                        return rank

                    def get_author(book):
                        author=info.split('|')[0]
                        return author

                    def get_publisher(book):
                        publisher = info.split('|')[1]
                        return publisher
                    def get_date(book):
                        date=info.split('|')[2]
                        return date

                    def get_price(book):
                        price = soup.find('span', {'class': 'ss_p2'}).b.find('span').text
                        return price
                    smu_genre = smu_genre_dict[smu_genre_num - 1]
                    aladin_genre = aladin_genre_dict[smu_genre_num - 1]

            #book_list.append(jsonObject['cryptoTopSearchRanks'][k][rank, title, author, publisher, date, star, aladin_genre, smu_genre, price])
            i += 1

for i in range(1, 3):
    driver.get("https://www.aladin.co.kr/shop/common/wbest.aspx?BestType=EBookBestseller&BranchType=9&CID="+str(smu_genre_id)+"&page="+str(i)+"&cnt=300&SortOrder=1")
    time.sleep(0.5)
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # 1위 책 클릭(대여 횟수 긁어오기 위함)
    books = soup.select('div.ss_book_box')
    def get_star(book):
        stars = book.select_one("div.ss_book_list img")
        if stars is None:
            return 0
        elif stars['src'] == "//image.aladin.co.kr/img/common/star_s10.gif":
            return 5
        elif stars['src'] == "//image.aladin.co.kr/img/common/star_s9.gif":
            return 4.5
        elif stars['src'] == "//image.aladin.co.kr/img/common/star_s8.gif":
            return 4
        elif stars['src'] == "//image.aladin.co.kr/img/common/star_s7.gif":
            return 3.5
        elif stars['src'] == "//image.aladin.co.kr/img/common/star_s6.gif":
            return 3
        elif stars['src'] == "//image.aladin.co.kr/img/common/star_s5.gif":
            return 2.5
        elif stars['src'] == "//image.aladin.co.kr/img/common/star_s4.gif":
            return 2
        else:
            return 0
    for book in books:
        try: #일반적인 경우
            title = book.select('a.bo3')[0].text

            li_tags = book.find_all('li')
            second_li_tag = li_tags[2] # 2. 두 번째 li 태그 선택
            info = second_li_tag.get_text() # 3. 두 번째 li 태그 내부의 첫 번째 내용 가져오기

            def get_title(book):
                    titles = soup.select('a.bo3')[0].text
                    return title
            def get_rank(book):
                ranks = book.select("td")[0].text
                return rank

            def get_author(book):
                authors=info.split('|')[0]
                return author

            def get_publisher(book):
                publishers = info.split('|')[1]
                return publisher
            def get_date(book):
                dates=info.split('|')[2]
                return date

            def get_price(book):
                prices = soup.find('span', {'class': 'ss_p2'}).b.find('span').text
                return price
            # author=info.split('|')[0]
            # publisher=info.split('|')[1]
            # date=info.split('|')[2] 
            # price = soup.find('span', {'class': 'ss_p2'}).b.find('span').text
            smu_genre = smu_genre_dict[smu_genre_num]            
            star = get_star(book)
            #rank = book.select("td")[0].text
                
            i += 1
            

        except IndexError: #행사 상품
            title = book.select('a.bo3')[0].text
            price = soup.find('span', {'class': 'ss_p2'}).b.find('span').text
            rank = book.select("td")[0].text
                
            star = get_star(book)
            try: #only 행사 상품
                li_tags = book.find_all('li')
                third_li_tag = li_tags[3] # 2. 두 번째 li 태그 선택
                info = third_li_tag.get_text() # 3. 두 번째 li 태그 내부의 첫 번째 내용 가져오기

                author=info.split('|')[0]
                publisher=info.split('|')[1]
                date=info.split('|')[2]
                smu_genre = smu_genre_dict[smu_genre_num]
                aladin_genre = aladin_genre_dict[smu_genre_num]
            
            except IndexError: #행사 상품은 아닌데, 출판사가 없음.
                second_li_tag = li_tags[2]
                info = second_li_tag.get_text()
                author=info.split('|')[0]
                publisher=None
                date=info.split('|')[1] 
                smu_genre = smu_genre_dict[smu_genre_num]
                aladin_genre = aladin_genre_dict[smu_genre_num]

        book_list.append([rank, title, author, publisher, date, star, aladin_genre, smu_genre, price])
        i += 1



dict_test =  {
    'col1' : rank,
    'col2' : title,
    'col3' : author,
    'col4' : publisher,
    'col5' : date,
    'col6' : star,
    'col7' : aladin_genre,
    'col8' : smu_genre,
    'col9' : price
}
# df_test = pd.DataFrame(dict_test)
# print(df_test)

df = pd.DataFrame(book_list, columns = ["순위", "제목", "알라딘_저자", "알라딘_출판사", "알라딘_출간일", "알라딘_별점", "알라딘_장르", "상명장르", "알라딘_가격"])

df.to_csv("알라딘_장르top100_11개" + '.csv', index = False, encoding = 'utf-8-sig')
print(df)