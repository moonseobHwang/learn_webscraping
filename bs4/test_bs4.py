from bs4 import BeautifulSoup

# from file
path = 'datas/sample02.html'
with open(path) as fp:
    soup = BeautifulSoup(fp, features='lxml')

    # Navigation Tree
    print(type(soup.title.parent.name), soup.title.parent.name)
    # <class 'str'> u'head'


