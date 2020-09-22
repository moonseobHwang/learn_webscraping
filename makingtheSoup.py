from bs4 import BeautifulSoup

path = 'datas/sample02.html' #from File

with open(path) as fp:       #Safe Return Resource
    soup = BeautifulSoup(fp, features='lxml')
    print(type(soup), soup)
# <class 'bs4.Beautifull'><html><body><p>a web page</p></body></html>

import requests
res = requests.get('https://www.google.com/')
print(res.status_code, res.content)

soup = BeautifulSoup(res.content, features='lxml')
print(type(soup), soup)
#200 b'<!doctype html><html itemscope="" itemtype="http://schema.org/..."
#...
#<class 'bs4.BeautifulSoup'><html><body><p>a wep page</p></body></html>
# 해보기
# Create Instance From URL (at least 3 site) and share source with google Doc