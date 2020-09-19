from bs4 import BeautifulSoup

# from file
path = 'datas/sample02.html'
with open(path) as fp:
    soup = BeautifulSoup(fp, features='lxml')
    # print(soup.prettify())
    soup.select(selector="title")
    # [<title>The Dormouse's story</title>]

    soup.select("p:nth-of-type(3)")
    # [<p class="story">...</p>]

    soup.select("body a")
    # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
    #  <a class="sister" href="http://example.com/lacie"  id="link2">Lacie</a>,
    #  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

    soup.select("html head title")
    # [<title>The Dormouse's story</title>]

    soup.select("head > title")
    # [<title>The Dormouse's story</title>]

    soup.select("p > a")
    # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
    #  <a class="sister" href="http://example.com/lacie"  id="link2">Lacie</a>,
    #  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

    soup.select("p > a:nth-of-type(2)")
    # [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

    soup.select("p > #link1")
    # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]

    soup.select("body > a")
    # []

    # Find the siblings of tags:
    soup.select("#link1 ~ .sister")
    # [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
    #  <a class="sister" href="http://example.com/tillie"  id="link3">Tillie</a>]

    soup.select("#link1 + .sister")
    # [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

    # Find tags by CSS class:
    soup.select(".sister")
    # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
    #  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
    #  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

    soup.select("[class~=sister]")
    # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
    #  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
    #  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

    # Find tags by ID:
    soup.select("#link1")
    # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]

    soup.select("a#link2")
    # [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

    # Find tags that match any selector from a list of selectors:
    soup.select("#link1,#link2")
    # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
    #  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

    # Test for the existence of an attribute:
    soup.select('a[href]')
    # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
    #  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
    #  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

    # Find tags by attribute value:
    soup.select('a[href="http://example.com/elsie"]')
    # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]

    soup.select('a[href^="http://example.com/"]')
    # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
    #  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
    #  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

    soup.select('a[href$="tillie"]')
    # [<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

    soup.select('a[href*=".com/el"]')
    # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]

    # If you’ve parsed XML that defines namespaces, you can use them in CSS selectors.:
    xml = '<tag xmlns:ns1="http://namespace1/" xmlns:ns2="http://namespace2/">  \
        <ns1:child>I\'m in namespace 1</ns1:child>   \
        <ns2:child>I\'m in namespace 2</ns2:child>   \
        </tag> '
    soup = BeautifulSoup(xml, "xml")

    soup.select("child")
    # [<ns1:child>I'm in namespace 1</ns1:child>, <ns2:child>I'm in namespace 2</ns2:child>]

    namespaces = dict(first="http://namespace1/", second="http://namespace2/")
    soup.select("ns1|child", namespaces=namespaces)
    # [<ns1:child>I'm in namespace 1</ns1:child>]