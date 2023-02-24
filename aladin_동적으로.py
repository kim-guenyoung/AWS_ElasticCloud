from bs4 import BeautifulSoup

import pandas as pd
import time
import requests
from datetime import datetime
import json
from datetime import datetime, timedelta

sm_genre_dict = { 
    3 : "가정/생활", #요리/살림
    4 : "가정/생활", #건강/취미
    5 : "경제/비즈니스", #경제/경영
    7 : "자연/과학", #과학, 사회과
    8 : "강의지원도서", #대학교재/전문서적
    10 : "문학", #소설/시/희곡
    12 : "인문", #사회과학
    15 : "에세이/산문", # 에세이, 자기계발
    18 : "문화/예술", # 예술/대중문화
    19 : "외국어", #외국어
    21 : "인문", #인문학
    23 : "에세이/산문",
    27 : "가정/생활", #좋은부모
    30 : "컴퓨터/인터넷", # 컴퓨터/모바일
}


aladin_genre_dict = { 
    3 : "요리/살림",
    4 : "건강/취미",
    5 : "경제경영",
    7 : "과학",
    8 : "대학교재/전문서적",
    10 : "소설/시/희곡",
    12 : "사회과학",
    15 : "에세이",
    18 : "예술/대중문화",
    19 : "외국어",
    21 : "인문학",
    23 : "자기계발",
    27 : "좋은 부모",
    30 : "컴퓨터/모바일"
}

_index = "aladin_best_100_test_"

# 칼럼 리스트 준비
book_list = []

present_date = str(datetime.utcnow() + timedelta(hours = 9))[:10]

response = requests.get("https://www.aladin.co.kr/shop/common/wbest.aspx?BestType=EBookBestseller&BranchType=9&CID=38409")
html_content = response.text

for sm_genre_num in range(3, 30):
    
    if(sm_genre_num == 3):
        sm_genre_id = 38409
        
    if(sm_genre_num == 6 or sm_genre_num == 9 or sm_genre_num == 11 or sm_genre_num == 13 or sm_genre_num == 14 or sm_genre_num == 16 or sm_genre_num == 17
       or sm_genre_num == 20 or sm_genre_num == 22 or sm_genre_num == 24 or sm_genre_num == 25 or sm_genre_num == 26 or sm_genre_num == 28
       or sm_genre_num == 29):
    # if(sm_genre_num == 6 or 9 or 11 or 13 or 14 or 16 or 17 or 20 or 22 or 24 or 25 or 28 or 29):
        sm_genre_num += 1
        continue

    elif(sm_genre_num == 4):
        sm_genre_id = 56388
    elif(sm_genre_num == 5):
        sm_genre_id = 38398
    elif(sm_genre_num == 6):
        sm_genre_id = 38414
    elif(sm_genre_num == 7):
        sm_genre_id = 38405
    elif(sm_genre_num == 8):
        sm_genre_id = 38422
   
    elif(sm_genre_num == 10):
        sm_genre_id = 38396

    elif(sm_genre_num == 12):
        sm_genre_id = 38404

    elif(sm_genre_num == 15):
        sm_genre_id = 56387

    elif(sm_genre_num == 18):
        sm_genre_id = 38402
    elif(sm_genre_num == 19):
        sm_genre_id = 38411

    elif(sm_genre_num == 21):
        sm_genre_id = 38403

    elif(sm_genre_num == 23):
        sm_genre_id = 38400

    elif(sm_genre_num == 27):
        sm_genre_id = 38413

        
    sm_genre_num += 1
    time.sleep(1)

    for i in range(1, 3):
        requests.get("https://www.aladin.co.kr/shop/common/wbest.aspx?BestType=EBookBestseller&BranchType=9&CID="+str(sm_genre_id)+"&page="+str(i)+"&cnt=300&SortOrder=1")
        time.sleep(0.5)

        url = "https://www.aladin.co.kr/shop/common/wbest.aspx?BestType=EBookBestseller&BranchType=9&CID=38409"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

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
                rank = book.select("td")[0].text
                
                li_tags = book.find_all('li')
                second_li_tag = li_tags[2] # 2. 두 번째 li 태그 선택
                info = second_li_tag.get_text() # 3. 두 번째 li 태그 내부의 첫 번째 내용 가져오기

                author=info.split('|')[0]
                publisher=info.split('|')[1]
                date=info.split('|')[2] 
                
                price = book.select("span.ss_p2 > b > span")[0].text
                sm_genre = sm_genre_dict[sm_genre_num - 1]
                aladin_genre = aladin_genre_dict[sm_genre_num - 1]
                
                star = get_star(book)
                
                i += 1
                

            except IndexError: #행사 상품
                title = book.select('a.bo3')[0].text
                price = book.select("span.ss_p2 > b > span")[0].text
                rank = book.select("td")[0].text
                
                star = get_star(book)
                try: #only 행사 상품
                    li_tags = book.find_all('li')
                    third_li_tag = li_tags[3] # 2. 두 번째 li 태그 선택
                    info = third_li_tag.get_text() # 3. 두 번째 li 태그 내부의 첫 번째 내용 가져오기

                    author=info.split('|')[0]
                    publisher=info.split('|')[1]
                    date=info.split('|')[2]
                    sm_genre = sm_genre_dict[sm_genre_num - 1]
                    aladin_genre = aladin_genre_dict[sm_genre_num - 1]
                    

                except IndexError: #행사 상품은 아닌데, 출판사가 없음.
                    second_li_tag = li_tags[2]
                    info = second_li_tag.get_text()
                    author=info.split('|')[0]
                    publisher=None
                    date=info.split('|')[1] 
                    sm_genre = sm_genre_dict[sm_genre_num - 1]
                    aladin_genre = aladin_genre_dict[sm_genre_num - 1]

               
            book_list.append([rank, title, author, publisher, date, price, star, aladin_genre, sm_genre, present_date])
            i += 1


for i in range(1, 3):
    
    url = "https://www.aladin.co.kr/shop/common/wbest.aspx?BestType=EBookBestseller&BranchType=9&CID=38401&page="+str(i)+"&cnt=300&SortOrder=1"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    time.sleep(0.5)
    
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
        title = book.select('a.bo3')[0].text
        price = book.select("span.ss_p2 > b > span")[0].text
        rank = book.select("td")[0].text
                
        star = get_star(book)
        try: #일반적인 경우
            
            li_tags = book.find_all('li')
            second_li_tag = li_tags[2] # 2. 두 번째 li 태그 선택
            info = second_li_tag.get_text() # 3. 두 번째 li 태그 내부의 첫 번째 내용 가져오기

            author=info.split('|')[0]
            publisher=info.split('|')[1]
            date=info.split('|')[2] 
            price = book.select("span.ss_p2 > b > span")[0].text
            sm_genre = sm_genre_dict[sm_genre_num]            
                
            i += 1
            

        except IndexError: #행사 상품
            sm_genre = sm_genre_dict[sm_genre_num]
            aladin_genre = aladin_genre_dict[sm_genre_num]
            try: #only 행사 상품
                li_tags = book.find_all('li')
                third_li_tag = li_tags[3] # 2. 두 번째 li 태그 선택
                info = third_li_tag.get_text() # 3. 두 번째 li 태그 내부의 첫 번째 내용 가져오기

                author=info.split('|')[0]
                publisher=info.split('|')[1]
                date=info.split('|')[2]
                
            
            except IndexError: #행사 상품은 아닌데, 출판사가 없음.
                second_li_tag = li_tags[2]
                info = second_li_tag.get_text()
                author=info.split('|')[0]
                publisher=None
                date=info.split('|')[1] 
                
            

        book_list.append([rank, title, author, publisher, date, price, star, aladin_genre, sm_genre, present_date])
        i += 1

df = pd.DataFrame(book_list, columns = ["aladin_rank", "subject", "aladin_writer", "aladin_publisher", "aladin_date","aladin_price", "aladin_review", "aladin_genre", "sm_genre", "present_date"])

df['present_date'] = present_date #time_stamp 속성 생성


# 데이터 전처리

df['aladin_rank'] = df["aladin_rank"].str.replace(pat = r'[^A-Za-z0-9가-힣]', repl = r' ', regex = True) #공백(엔터)

df['aladin_price'] = df['aladin_price'].str.replace(pat=',', repl = '',regex=True) #, 삭제
df['aladin_price'] = pd.to_numeric(df['aladin_price'])


df['aladin_date'] = df['aladin_date'].str.replace(pat='년 ', repl = '-',regex=True)#년 -> -
df['aladin_date'] = df['aladin_date'].str.replace(pat='월', repl = '',regex=True) #월 -> 

df['aladin_date'] = df['aladin_date'].str.strip()
df['aladin_date'] = pd.to_datetime(df['aladin_date'])

df.to_csv(f"{_index + present_date}.csv", index = False, encoding = 'utf-8-sig')
df2 = df

from elasticsearch import Elasticsearch, helpers
import configparser

config = configparser.ConfigParser()
config.read('example.ini')

es = Elasticsearch(
    cloud_id=config['ELASTIC']['cloud_id'],
    http_auth=(config['ELASTIC']['user'], config['ELASTIC']['password'])
)

if es.indices.exists(index = _index + present_date):
    pass
else:
    resp = es.indices.create(index = _index + present_date, body = {
        "settings": {
            "analysis": {
                "analyzer": {
                    "nori": {
                        "tokenizer": "nori_tokenizer"
                    }
                }
            }
        },
        "mappings": {
            "properties": {
                "aladin_rank" : {
                    "type" : "integer"
                },
                "subject": {
                    "type": "text",
                    "analyzer": "nori",
                    "fields":{
                        "keyword":{
                            "type":"keyword"
                        }
                    }
                },
                "aladin_genre": {
                    "type": "keyword"
                },
                "aladin_writer": {
                    "type": "text",
                    "analyzer": "nori",
                    "fields":{
                        "keyword":{
                            "type":"keyword"
                        }
                    }
                },
                "aladin_publisher": {
                    "type": "text",
                    "analyzer": "nori",
                    "fields":{
                        "keyword":{
                            "type":"keyword"
                        }
                    }
                },
                "aladin_date": {
                    "type": "text",
                    "fields" : {
                        "keyword" : {
                            "type" : "keyword"
                        }
                    }
                },
                "sm_genre": {
                    "type": "keyword"
                },
                "aladin_price": {
                    "type": "integer"
                },
                "aladin_review": {
                    "type": "float"
                },
                "present_date": {
                    "type": "date"
                }
            }
        }
    })

for k in range(len(df2)) :
    es.index(index= _index + present_date,
         document = {
         "aladin_rank" : str(df2.loc[k].aladin_rank),
         "subject" : str(df2.loc[k].subject),
         "aladin_writer": str(df2.loc[k].aladin_writer),
         "aladin_publisher": str(df2.loc[k].aladin_publisher),
         "aladin_date": str(df2.loc[k].aladin_date),
         "aladin_price": str(df2.loc[k].aladin_price),
         "aladin_review": str(df2.loc[k].aladin_review),
         "aladin_genre": str(df2.loc[k].aladin_genre),
         "sm_genre": str(df2.loc[k].sm_genre),
         "present_date": present_date
 })