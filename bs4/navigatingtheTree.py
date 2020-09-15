from bs4 import BeautifulSoup

# from file
path = 'datas/sample02.html'
with open(path) as fp:
    soup = BeautifulSoup(fp, features='lxml')
    # print(soup.prettify())
    
    # Navigating using tag names
    # print(soup.head)
    # # <head><title>The Dormouse's story</title></head>
    # print(soup.title)
    # # <title>The Dormouse's story</title>
    # print(soup.body.b)
    # # <b>The Dormouse's story</b>
    # print(soup.a)
    # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

    print('-'*30)
    # Going down - .contents and .children
    body_tag = soup.body
    print(type(body_tag), '\n', '-'*30)
    for child in body_tag.children:
        print(type(child), child)

    # Going up
    