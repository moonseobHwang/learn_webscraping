import requests
from bs4 import BeautifulSoup
res = requests.get('http://media.daum.net/economic/')
# print(type(res), res.status_code, res.content)
soup = BeautifulSoup(res.content, 'html.parser')
links = soup.select('a[href]')
print(type(links), len(links))		
# <class 'list'> 233
print(links)
for link in links:
    print(type(link),link)      
    # <class 'bs4.element.Tag'> <a href="#kakaoBody">본문 바로가기</a> ...
