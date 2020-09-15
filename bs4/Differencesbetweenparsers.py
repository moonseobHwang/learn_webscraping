from bs4 import BeautifulSoup

print('html.parser : ', BeautifulSoup("<a><b/></a>", "html.parser"))
# <a><b></b></a>
print('html.parser : ', BeautifulSoup("<a></p>", "html.parser"))
# <a></a>

print('xml : ', BeautifulSoup("<a><b/></a>", "xml"))
# <?xml version="1.0" encoding="utf-8"?>
# <a><b/></a>

print('lxml : ', BeautifulSoup("<a><b/></a>", "lxml"))
# <html><body><a></a></body></html>
print('lxml : ', BeautifulSoup("<head/><a></p>", "lxml"))
# <html><head></head><body><a></a></body></html>

print('html5lib : ', BeautifulSoup("<head/><a></p>", "html5lib"))
# <html><head></head><body><a><p></p></a></body></html>

path = 'datas/sample01.json'					# from File
with open(path) as fp:							# Safe Return Resource
    print('html.parser : ', BeautifulSoup(fp, "html.parser"))
    print('xml: ', BeautifulSoup(fp, "xml"))
    print('lxml : ', BeautifulSoup(fp, "lxml"))
    print('html5lib : ', BeautifulSoup(fp, "html5lib"))

