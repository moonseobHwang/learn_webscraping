from bs4 import BeautifulSoup

path = 'datas/sample02.html' #from File

with open(path) as fp:       #Safe Return Resource
    soup = BeautifulSoup(fp, features='lxml')
    print(type(soup), soup)
# <class 'bs4.Beautifull'><html><body><p>a web page</p></body></html>

import requests
res = requests.get('https://www.google.com/search?q=%EC%B7%A8%EC%97%85%EC%82%AC%EC%9D%B4%ED%8A%B8&oq=%EC%B7%A8%EC%97%85%EC%82%AC%EC%9D%B4%ED%8A%B8&aqs=chrome..69i57.2150j0j15&sourceid=chrome&ie=UTF-8')
print(res.status_code, res.content)

soup = BeautifulSoup(res.content, features='lxml')
print(type(soup.a), soup.a)
#200 b'<!doctype html><html itemscope="" itemtype="http://schema.org/..."
#...
#<class 'bs4.BeautifulSoup'><html><body><p>a wep page</p></body></html>
# 해보기
# Create Instance From URL (at least 3 site) and share source with google Doc