from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import os
import pandas as pd
from urllib.request import urlopen
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C:/Users/김근영/chromedriver_win32.zip/chromedriver.exe")
# 교보문고의 베스트셀러 웹페이지를 가져옵니다.
driver.get("https://libnt.smuc.ac.kr/Search/BestBook50?stdate=&eddate=&strclass=")
bsObject = BeautifulSoup(driver.page_source, 'html.parser')

# while(True):
#     category=bsObject.find('div', 'sponge-page-guide').find('div', 'book-title-page').find('dl', 'row').select_one("dd.col-md-8").text

while(True):

    # 리뷰 리스트 가져오기
    content_list =  soup.find('div',class_='book-title-page').find('dl', class_ = 'row').find_all('dd', class_ = 'col-md-8')

    for dd in content_list:


        # 각 요소 가져오기
        tmp_score = dd.find('div', class_='star_score').find('em').text
        # tmp_text = li.find('div', class_='score_reple').find('p').text
        # tmp_user = li.find('div', class_='score_reple').find('dl').find('span').text
        # tmp_date = li.find('div', class_='score_reple').find_all('em')[1].text
        # tmp_good = li.find('div', class_='btn_area').find_all('strong')[0].text
        # tmp_bad = li.find('div', class_='btn_area').find_all('strong')[1].text

        # 칼럼 리스트에 추가
        score.append(tmp_score)
        text.append(tmp_text)
        user.append(tmp_user)
        date.append(tmp_date)
        good.append(tmp_good)
        bad.append(tmp_bad)

        # 확인용 프린트
        print("총 %s 건 중 %s 번째 리뷰 데이터를 수집합니다===================================="%(input_num, count))
        print('1) 별점:', tmp_score)
        print('2) 리뷰내용:', tmp_text)
        print('3) 작성자:', tmp_user)
        print('4) 작성일자:', tmp_date)
        print('5) 공감:', tmp_good)
        print('6) 비공감:',tmp_bad)
        print('\n')

        # txt파일에 저장
        f = open(f_txt, 'a',encoding='UTF-8')
        f.write("총 %s 건 중 %s 번째 리뷰 데이터를 수집합니다===================================="%(input_num, count) + '\n')
        f.write('1) 별점: ' + tmp_score + '\n')
        f.write('2) 리뷰내용: ' + tmp_text + '\n')
        f.write('3) 작성자: ' + tmp_user + '\n')
        f.write('4) 작성일자: ' + tmp_date + '\n')
        f.write('5) 공감: ' + tmp_good + '\n')
        f.write('6) 비공감: ' + tmp_bad + '\n')
        f.write('\n')

        # 만약 현재 글 수가 입력건수에 도달하면 루프 종료
        if(count == input_num):
            break
    
    if(count == input_num):
        break
    
    # 아직 입력건수에 도달하지 않았다면 다음 페이지를 열고 루프 계속
    else:
        driver.find_element_by_class_name('pg_next').click()
        time.sleep(1)
                
        driver.switch_to_default_content()
        driver.switch_to_frame('pointAfterListIframe')

        full_html = driver.page_source
        soup = BeautifulSoup(full_html, 'html.parser')
