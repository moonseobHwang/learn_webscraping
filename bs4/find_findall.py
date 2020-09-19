from bs4 import BeautifulSoup

# from file
path = 'datas/sample02.html'
with open(path) as fp:
    soup = BeautifulSoup(fp, features='lxml')
    # soup = BeautifulSoup(fp, features='html.parser')
    # print(type(soup), soup)

    print(type(soup.get_text()), soup.get_text())
    # <class 'str'> The Dormouse's story ... 

    print(type(soup.find(id="link3")), soup.find(id="link3"))
    # class 'bs4.element.Tag'> <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>

    print(type(soup.find_all(name='a')), soup.find_all(name='a'))
    # <class 'bs4.element.ResultSet'> [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
    #  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
    #  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

    print(type(soup.find_all(name='b')), soup.find_all(name='b'))
    # <class 'bs4.element.ResultSet'> [<b>The Dormouse's story</b>]

    print(type(soup.find_all(name=["a", "b"])), soup.find_all(name=["a", "b"]))
    # <class 'bs4.element.ResultSet'> [<b>The Dormouse's story</b>,
    #  <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
    #  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
    #  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

    print(type(soup.find_all(id=True)), soup.find_all(id=True))
    # <class 'bs4.element.ResultSet'> [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
    #  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
    #  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

    find_attrs = soup.find_all(name='a', attrs={"href": True})
    print(type(find_attrs), find_attrs)
    # <class 'bs4.element.ResultSet'> [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
    #  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
    #  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

    find_attrs = soup.find_all(name='a', attrs={"class": 'sister', 'id':['link2','link3']})
    print(type(find_attrs), find_attrs)

    import re
    result = soup.find_all(name=re.compile("^b"))
    print(type(result), result)
    # <class 'bs4.element.ResultSet'> [<body> <p class="title"> ..., <b>The Dormouse's story</b>]
    for tag in result:
        print(type(tag), tag, type(tag.name), tag.name)
    # <class 'bs4.element.Tag'> <body> ... </body> <class 'str'> body
    # <class 'bs4.element.Tag'> <b>The Dormouse's story</b> <class 'str'> b
    taglist = result[0].find_all('a')
    print(type(taglist), taglist)
    # <class 'bs4.element.ResultSet'> [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
    #  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
    #  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

    result = soup.find_all(name=re.compile("t"))
    for tag in result:
        print(type(tag), tag, type(tag.name), tag.name)
        # <class 'str'> html
        # <class 'str'> title