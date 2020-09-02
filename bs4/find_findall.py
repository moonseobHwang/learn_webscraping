from bs4 import BeautifulSoup

# from file
path = 'datas/sample02.html'
with open(path) as fp:
    soup = BeautifulSoup(fp, features='lxml')
    # soup = BeautifulSoup(fp, features='html.parser')
    # print(type(soup), soup)

    print(type(soup.find_all('a')), soup.find_all('a'))
    # <class 'bs4.element.ResultSet'> [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
    #  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
    #  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

    print(type(soup.find(id="link3")), soup.find(id="link3"))
    # <class 'bs4.element.Tag'> <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>

    print(type(soup.get_text()), soup.get_text())
    # <class 'str'> The Dormouse's story ... 

    print(type(soup.find_all('b')), soup.find_all('b'))
    # [<b>The Dormouse's story</b>]

    import re
    result = soup.find_all(re.compile("^b"))
    print(type(result), result)
    # <class 'bs4.element.ResultSet'> [<body> <p class="title"> ..., <b>The Dormouse's story</b>]

    for tag in result:
        print(type(tag.name), tag.name)
    # <class 'str'> body
    # <class 'str'> b

    result = soup.find_all(re.compile("t"))
    for tag in result:
        print(type(tag.name), tag.name)
    # <class 'str'> html
    # <class 'str'> title

    print(type(soup.find_all(["a", "b"])), soup.find_all(["a", "b"]))
    # <class 'bs4.element.ResultSet'> [<b>The Dormouse's story</b>,
    #  <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
    #  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
    #  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]