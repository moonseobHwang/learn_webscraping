from bs4 import BeautifulSoup

# from string
source_html = '<html><head></head><body>Sacr&eacute; bleu!</body></html>'
soup = BeautifulSoup(markup=source_html)
print(type(soup), soup)

# from file
path = 'datas/sample01.html'
with open(path) as fp:
    soup = BeautifulSoup(fp, features='lxml')
    print(type(soup), soup)

# from url
import requests
res = requests.get('https://www.google.com/')
print(res.status_code, res.content)
soup = BeautifulSoup(res.content, features='lxml')
print(type(soup), soup.prettify())
