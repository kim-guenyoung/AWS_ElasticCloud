import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

# 책 제목 : yDetailTopWrap > div.topColRgt > div.gd_infoTop > div > h2
# 저자 명 :	yDetailTopWrap > div.topColRgt > div.gd_infoTop > span.gd_pubArea > span.gd_auth > a
# 출판사 명 : yDetailTopWrap > div.topColRgt > div.gd_infoTop > span.gd_pubArea > span.gd_pub > a
# 출간일 : yDetailTopWrap > div.topColRgt > div.gd_infoTop > span.gd_pubArea > span.gd_date
# 판매지수 : yDetailTopWrap > div.topColRgt > div.gd_infoTop > span.gd_ratingArea > span.gd_sellNum
# 정가 : yDetailTopWrap > div.topColRgt > div.gd_infoBot > div.gd_infoTbArea > div:nth-child(3) > table > tbody > tr:nth-child(1) > td > span > em
# 판매가 : yDetailTopWrap > div.topColRgt > div.gd_infoBot > div.gd_infoTbArea > div:nth-child(3) > table > tbody > tr.accentRow > td > span > em

# url = 'http://www.yes24.com/Product/Goods/71933018'
# res = requests.post(url)
# soup = BeautifulSoup(res.text, 'html.parser')
# tag_name = '#yDetailTopWrap > div.topColRgt > div.gd_infoTop > div > h2'
# books = soup.select(tag_name)
# book_name = books[0].text
# print(book_name)

# 데이터 수집 함수 정의
def yes24DataReader(CategoryNumber, year, month):
    
    root_url = 'http://www.yes24.com'

    url_1 = 'http://www.yes24.com/24/category/bestseller?CategoryNumber=001&sumgb=06'
    
    url_2 = '&PageNumber='
   
    url_3 =  '&FetchSize=80'
    
    i = 1

    url_set = url_1 + url_2 + str(i) + url_3
    print(url_set)

    book_list=[]
    #category_layout > tbody > tr:nth-child(1) > td.goodsTxtInfo
    # 월 별 조회 시 최대 50쪽이지만, 간단한 설명을 위해 2쪽까지만 수집
    for i in range(1, 3):

        url = url_set + str(i)

        res = requests.post(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        tag = '#category_layout > tbody > tr:nth-child(1) > td.goodsTxtInfo'
        books = soup.select(tag)

        # 수집 중인 페이지 번호 출력
        print('# Page', i)

        # 개별 도서 정보 수집
        for book in books:

            sub_url = root_url + book.attrs['href']
            sub_res = requests.post(sub_url)
            sub_soup = BeautifulSoup(sub_res.text, 'html.parser')

            tag_name = '#category_layout > tbody > tr:nth-child(1) > td.goodsTxtInfo > p:nth-child(1)'
            tag_author = '#yDetailTopWrap > div.topColRgt > div.gd_infoTop > span.gd_pubArea > span.gd_auth > a'
            tag_author2 = '#yDetailTopWrap > div.topColRgt > div.gd_infoTop > span.gd_pubArea > span.gd_auth'
            tag_publisher = '#yDetailTopWrap > div.topColRgt > div.gd_infoTop > span.gd_pubArea > span.gd_pub > a'
            tag_date = '#yDetailTopWrap > div.topColRgt > div.gd_infoTop > span.gd_pubArea > span.gd_date'
            tag_sales = '#yDetailTopWrap > div.topColRgt > div.gd_infoTop > span.gd_ratingArea > span.gd_sellNum'

            tag_listprice = '#yDetailTopWrap > div.topColRgt > div.gd_infoBot > div.gd_infoTbArea > div:nth-child(3) > table > tbody > tr:nth-child(1) > td > span > em'
            tag_listprice2 = '#yDetailTopWrap > div.topColRgt > div.gd_infoBot > div.gd_infoTbArea > div:nth-child(4) > table > tbody > tr:nth-child(1) > td > span > em'
            tag_price = '#yDetailTopWrap > div.topColRgt > div.gd_infoBot > div.gd_infoTbArea > div:nth-child(3) > table > tbody > tr:nth-child(2) > td > span > em'
            tag_price2 = '#yDetailTopWrap > div.topColRgt > div.gd_infoBot > div.gd_infoTbArea > div:nth-child(4) > table > tbody > tr:nth-child(2) > td > span > em'

            tag_page = '#infoset_specific > div.infoSetCont_wrap > div > table > tbody > tr:nth-child(2) > td'
            tag_weight = '#infoset_specific > div.infoSetCont_wrap > div > table > tbody > tr:nth-child(2) > td'
            tag_hor = '#infoset_specific > div.infoSetCont_wrap > div > table > tbody > tr:nth-child(2) > td'
            tag_ver = '#infoset_specific > div.infoSetCont_wrap > div > table > tbody > tr:nth-child(2) > td'
            tag_width = '#infoset_specific > div.infoSetCont_wrap > div > table > tbody > tr:nth-child(2) > td'
            tag_isbn13 = '#infoset_specific > div.infoSetCont_wrap > div > table > tbody > tr:nth-child(3) > td'
            tag_isbn10 = '#infoset_specific > div.infoSetCont_wrap > div > table > tbody > tr:nth-child(4) > td'


            # 기본적인 예외처리를 통한 데이터 수집
            name = sub_soup.select(tag_name)[0].text

            try:
                author = sub_soup.select(tag_author)[0].text
            except:
                author = sub_soup.select(tag_author2)[0].text.strip('\n').strip().replace(' 저','')


            publisher = sub_soup.select(tag_publisher)[0].text
            date = sub_soup.select(tag_date)[0].text.replace('년 ','-').replace('월 ','-').replace('일','')

            try:
                sales = sub_soup.select(tag_sales)[0].text
                if '판매지수' in sales:
                    sales = sub_soup.select(tag_sales)[0].text.strip().strip('|').strip().lstrip('판매지수 ').rstrip(' 판매지수란?')
                else :
                    sales =''
            except:
                sales = ''

            try:
                listprice = sub_soup.select(tag_listprice)[0].text.replace(',','').replace('원','')
            except:
                try:
                    listprice = sub_soup.select(tag_listprice2)[0].text.replace(',','').replace('원','')
                except:
                    listprice = ''

            try:
                price = sub_soup.select(tag_price)[0].text.replace(',','')
            except:
                try:
                    price = sub_soup.select(tag_price2)[0].text.replace(',','')
                except:
                    price = ''

            page = sub_soup.select(tag_page)[0].text
            if '쪽' in page:
                if '확인' in page:
                    page = ''
                else :
                    page = page.split('|')[0].strip().replace('쪽','')
            else :
                page = ''

            weight = sub_soup.select(tag_weight)[0].text
            if 'g' in weight:
                weight = weight[:weight.find('g')].split('|')[1].strip()
            else :
                weight = ''

            hvw = sub_soup.select(tag_hor)[0].text
            if 'mm' in hvw:

                if hvw.split('|')[-1].strip().count('*')==2:

                    hor = hvw.split('|')[-1].strip().split('*')[0]
                    ver = hvw.split('|')[-1].strip().split('*')[1]
                    width = hvw.split('|')[-1].strip().split('*')[2].replace('mm','')

                elif hvw.split('|')[-1].strip().count('*')==1:

                    hor = hvw.split('|')[-1].strip().split('*')[0]
                    ver = hvw.split('|')[-1].strip().split('*')[1].replace('mm','')
                    width = ''

            else :
                hor = ''
                ver = ''
                width = ''

            try :
                isbn13 = sub_soup.select(tag_isbn13)[0].text
                if '확인' in isbn13:
                    isbn13 = ''
                else :
                    isbn13 = sub_soup.select(tag_isbn13)[0].text
            except :
                isbn13 = ''


            try :
                isbn10 = sub_soup.select(tag_isbn10)[0].text
                if '확인' in isbn10:
                    isbn10 = ''
                else :
                    isbn10 = sub_soup.select(tag_isbn10)[0].text
            except :
                isbn10 = ''

            book_list.append([name, author, publisher, date,
                              sales, listprice, price, page,
                              weight, hor, ver, width, isbn13, isbn10])

            print('=========>', name)

    # 데이터프레임 컬럼명 지정
    colList = ['name',  'author', 'publisher', 'date',
               'sales', 'listprice', 'price', 'page',
               'weight', 'hor', 'ver', 'width', 'isbn13', 'isbn10']

    # 데이터프레임으로 변환
    df = pd.DataFrame(book_list, columns=colList)

    return df

# 역사 카테고리 번호 : 001001010
CategoryNum='001001010'

# 2019년도
for year in range(2019, 2020):
    print('='*50)
    print('# Year', year)
    print('='*50)

    # 9월
    for month in range(9, 10):
        print('='*50)
        print('# Month', month)
        print('='*50)

        # 월 별 데이터 수집
        df = yes24DataReader(CategoryNum, str(year), str(month))

        # 월 별로 수집된 데이터를 CSV 형식 파일로 저장
        df.to_csv(str(year)+'_'+str(month)+'_'+str(CategoryNum)+'.csv', index=False, encoding='CP949')