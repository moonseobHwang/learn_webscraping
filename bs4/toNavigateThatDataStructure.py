from bs4 import BeautifulSoup

# from file
path = 'datas/sample02.html'
with open(path) as fp:
    soup = BeautifulSoup(fp, features='lxml')
    # soup = BeautifulSoup(fp, features='html.parser')
    # print(type(soup), soup)
    print(type(soup.title), soup.title)
    # <class 'bs4.element.Tag'> <title>The Dormouse's story</title>

    print(type(soup.title.name), soup.title.name)
    # <class 'str'> u'title'

    print(type(soup.title.string), soup.title.string)
    # <class 'bs4.element.NavigableString'> u'The Dormouse's story'

    print(type(soup.title.parent.name), soup.title.parent.name)
    # <class 'str'> u'head'

    print(type(soup.p), soup.p)
    # <class 'bs4.element.Tag'> <p class="title"><b>The Dormouse's story</b></p>

    print(type(soup.p['class']), soup.p['class'])
    # <class 'list'> u'title'

    print(type(soup.a), soup.a)
    # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

    print(type(soup.find_all('a')), soup.find_all('a'))
    # <class 'bs4.element.ResultSet'> [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
    #  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
    #  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

    print(type(soup.find(id="link3")), soup.find(id="link3"))
    # <class 'bs4.element.Tag'> <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>

    print(type(soup.get_text()), soup.get_text())
    # <class 'str'> The Dormouse's story ... 