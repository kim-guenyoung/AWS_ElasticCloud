# #구현하고 싶은 것
# 1. 교보문고 사이트 들어간 뒤에 몇 권을 검색하고 싶은 지 사용자에게 입력받고
# 2. 입력받은 걸 토대로 그 값만큼 크롤링해오기
# (교보문고 베스트 코너에 들어가면 20개씩 보기, 50개씩 보기가 있는데 만약 20개씩 보기를 선택한 상태에서
#  30권을 가져오게 하고 싶으면 driver.find_element('pg_next').click() 코드를 이용해 다음 장으로 넘어가 10권의 책을 더 불러와야함.)
# 3. csv 파일로 변환해서 자동으로 저장되게
# ++참고사항 : kyobo.py는 인터넷에서 불러온 소스코드이고, best20까지 됨.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import os
import pandas as pd
from urllib.request import urlopen
import time
from selenium.webdriver.common.by import By



while(True):
    input_num = input("크롤링할 베스트셀러는 몇 건입니까?")
    try:
        input_num = int(input_num)
        break
    except:
        print('다시 입력해주세요.')
        continue

input_path = input('3. 파일을 저장할 폴더명만 쓰세요: ')

driver = webdriver.Chrome(ChromeDriverManager().install())
#driver = webdriver.Chrome(executable_path= 'C:/Users/김근영/chromedriver_win32.zip/chromedriver.exe')
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver = webdriver.Chrome(os.getcwd() + "/chromedriver.exe")
url = "https://www.kyobobook.co.kr/"
driver.get(url)

# 교보문고의 베스트셀러 웹페이지를 가져옵니다.
driver.get("https://product.kyobobook.co.kr/bestseller/online?period=001")
bsObject = BeautifulSoup(driver.page_source, 'html.parser')

#칼럼 리스트 준비
score = []
title = []
author = []
#데이터프레임 생성, 각 칼럼 리스트 넣기
df = pd.DataFrame()
df['별점'] = score
df['제목'] = title
df['저자'] = author

for i in range(len(df)):
    df['내용'][i] = df['내용'][i].replace("\t", "")
    df['내용'][i] = df['내용'][i].replace("\n", "")
#크롤링한 책 수 카운트
count = 0

if(input_path == '0'):
    input_path = os.getcwd()

# 전체 소스 가져오기
full_html = driver.page_source
soup = BeautifulSoup(full_html, 'html.parser')

book_page_urls = []
# 책의 상세 웹페이지 주소를 추출하여 리스트에 저장합니다.
while(True):

# 책 정보 리스트 가져오기
    #content_list =  soup.find('div',class_='ifr_area basic_ifr').find('div', class_ = 'score_result').find('ul').find_all('li')
    for item in bsObject.find_all('div', 'prod_info_box'):
        url = item.select('a')[0].get('href')
        book_page_urls.append(url)

        count += 1

        if(count == input_num):
            break

    if(count == input_num):
        break
        
        # 아직 입력건수에 도달하지 않았다면 다음 페이지를 열고 루프 계속
    else:
        driver.find_element('pg_next').click()
        #driver.find_element_by_class_name('pg_next').click()
        time.sleep(1)
                
        driver.switch_to_default_content()
        driver.switch_to_frame('pointAfterListIframe')

        full_html = driver.page_source
        soup = BeautifulSoup(full_html, 'html.parser')

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


#각 파일경로와 파일이름 설정
f_txt = input_path + '/' + title + '_' + '.txt'
f_csv = input_path + '/' + title + '_' + '.txt'
f_xls = input_path + '/' + title + '_' + '.txt'

df.to_excel(f_xls,encoding="utf-8-sig",index=True)
df.to_csv(f_csv,encoding="utf-8-sig",index=True)

data = pd.read_csv(f'./{input_title}/{input_path}_.csv')

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import os
import pandas as pd
from urllib.request import urlopen
import time
from selenium.webdriver.common.by import By



while(True):
    input_num = input("크롤링할 베스트셀러는 몇 건입니까?")
    try:
        input_num = int(input_num)
        break
    except:
        print('다시 입력해주세요.')
        continue

input_path = input('3. 파일을 저장할 폴더명만 쓰세요: ')

driver = webdriver.Chrome(ChromeDriverManager().install())
#driver = webdriver.Chrome(executable_path= 'C:/Users/김근영/chromedriver_win32.zip/chromedriver.exe')
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver = webdriver.Chrome(os.getcwd() + "/chromedriver.exe")
url = "https://www.kyobobook.co.kr/"
driver.get(url)

# 교보문고의 베스트셀러 웹페이지를 가져옵니다.
driver.get("https://product.kyobobook.co.kr/bestseller/online?period=001")
bsObject = BeautifulSoup(driver.page_source, 'html.parser')

#칼럼 리스트 준비
score = []
title = []
author = []
#데이터프레임 생성, 각 칼럼 리스트 넣기
df = pd.DataFrame()
df['별점'] = score
df['제목'] = title
df['저자'] = author

for i in range(len(df)):
    df['내용'][i] = df['내용'][i].replace("\t", "")
    df['내용'][i] = df['내용'][i].replace("\n", "")
#크롤링한 책 수 카운트
count = 0

if(input_path == '0'):
    input_path = os.getcwd()

# 전체 소스 가져오기
full_html = driver.page_source
soup = BeautifulSoup(full_html, 'html.parser')

book_page_urls = []
# 책의 상세 웹페이지 주소를 추출하여 리스트에 저장합니다.
while(True):

# 책 정보 리스트 가져오기
    #content_list =  soup.find('div',class_='ifr_area basic_ifr').find('div', class_ = 'score_result').find('ul').find_all('li')
    for item in bsObject.find_all('div', 'prod_info_box'):
        url = item.select('a')[0].get('href')
        book_page_urls.append(url)

        count += 1

        if(count == input_num):
            break

    if(count == input_num):
        break
        
        # 아직 입력건수에 도달하지 않았다면 다음 페이지를 열고 루프 계속
    else:
        driver.find_element('pg_next').click()
        #driver.find_element_by_class_name('pg_next').click()
        time.sleep(1)
                
        driver.switch_to_default_content()
        driver.switch_to_frame('pointAfterListIframe')

        full_html = driver.page_source
        soup = BeautifulSoup(full_html, 'html.parser')

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


#각 파일경로와 파일이름 설정
f_txt = input_path + '/' + title + '_' + '.txt'
f_csv = input_path + '/' + title + '_' + '.txt'
f_xls = input_path + '/' + title + '_' + '.txt'

df.to_excel(f_xls,encoding="utf-8-sig",index=True)
df.to_csv(f_csv,encoding="utf-8-sig",index=True)

data = pd.read_csv(f'./{input_title}/{input_path}_.csv')