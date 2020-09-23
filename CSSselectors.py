import requests
from bs4 import BeautifulSoup
res = requests.get("http://news.daum.net/economic")
res.status_code,res.content
soup = BeautifulSoup(res.content, 'lxml')
links = soup.select('a[href]')
for link in links:
    print(type(links), len(links))
    break