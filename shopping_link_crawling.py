from bs4 import BeautifulSoup
import requests

encText= "검색할 상품"
# 리뷰순
url = 'https://search.shopping.naver.com/search/all?origQuery=%EC%82%AC%EA%B3%BC&pagingIndex=1&pagingSize=40&productSet=total&query='+encText+'&sort=review&timestamp=&viewType=list'
# 랭킹순
#url = "https://search.shopping.naver.com/search/all?query=" + encText
html = requests.get(url)
soup = BeautifulSoup(html.text, 'lxml')
cnt = len(soup.find_all('div', class_='basicList_title__3P9Q7'))

# 사용자에게 보여질 link 목록
shopping_link = []

for i in range(0, cnt):
    show = {}
    metadata = soup.find_all('div', class_='basicList_title__3P9Q7')[i]
    title = metadata.a.get('title')
    print("<제품명> : ", title)  # title

    price = soup.find_all('span', class_='price_num__2WUXn')[i].text
    print("<가격> : ", price)  # 가격

    url = metadata.a.get('href')
    print("<url> : ", url)  # url
    shopping_link.append(url)
    print("===================================================")

    show = {'제품명': title, '가격': price, 'url': url}

print(shopping_link)