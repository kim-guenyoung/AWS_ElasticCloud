import requests
from bs4 import BeautifulSoup
import re
from selenium.webdriver.common.by import By
def no_space(text):
    text1 = re.sub('&nbsp; | &nbsp;| \n|\t|\r','',text)
    text2 = re.sub('\n\n', '', text1)
    return text2

url = 'http://www.yes24.com/24/category/bestseller?CategoryNumber=017&sumgb=08&FetchSize=20&PageNumber=2'
res = requests.get(url)

soup = BeautifulSoup(res.text, 'html.parser')
books = soup.select('td.goodsTxtInfo')
book_list = []
#print(books)
i = 1
for book in books:
    dd = book.select('td.goodsTxtInfo > p')[0].text
    #company = book.select('div > a')[1].text
    title = book.select('p > a')[0].text
    writer = book.select('div > a')[0].text
    price = book.select('span.priceB')[0].text

    #writer = book.select('div')[0].text.split('|')
    # writer = str(writer)
    # writer = re.sub(r"\s", "", writer)
    # writer_list = []
    # for k in writer:
    #     writer = str(k).strip('\n\r''')
    #     writer_list.append(writer)
    
    

    
    print(str(i) + ' | ' + title + ' | '+ writer + ' | ' + str(price) + ' | ')
    book_list.append([str(i),title,writer,price])
    i+=1


import pandas as pd
df = pd.DataFrame(book_list, columns=['rank','title','writer','price'])
df.to_csv('jinseok1.csv',encoding='cp949', index=False)

