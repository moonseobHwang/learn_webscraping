from bs4 import BeautifulSoup

# from file
path = 'datas/sample02.html'
with open(path) as fp:
    soup = BeautifulSoup(fp, features='lxml')
    # print(soup.prettify())

    # print('-'*30)

    # Going down - .contents and .children
    body_tag = soup.body
    print(type(body_tag), '\n', '-'*30)
    # <class 'bs4.element.Tag'> 
    bodychildren = body_tag.children
    print(type(bodychildren), len(list(bodychildren)))
    # <class 'list_iterator'> 7
    for child in body_tag.children:
        print(type(child), repr(child))
        # <class 'bs4.element.NavigableString'>
        # <class 'bs4.element.Tag'> <p class="title"><b> ...
        # <class 'bs4.element.NavigableString'> ...
        # ...
        # <class 'bs4.element.NavigableString'>

    # Going up
    # .parent
    title_tag = soup.title
    print(type(title_tag), title_tag)
    # <class 'bs4.element.Tag'> <title>The Dormouse's story</title>
    print(type(title_tag.parent), title_tag.parent)
    # <class 'bs4.element.Tag'> <head><title>The Dormouse's story</title></head>
    print(type(title_tag.string.parent), title_tag.string.parent)
    # <<class 'bs4.element.Tag'>  title>The Dormouse's story</>
    # .parents
    link = soup.a
    print(type(link), link)
    # <class 'bs4.element.Tag'> <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
    print(type(link.parents), len(list(link.parents)))  
    # <class 'generator'> 4     # generator function that behaves like an iterator
    for parent in link.parents:
        if parent is None:
            print(type(parent), parent)
        else:
            print(type(parent.name), parent.name)
        # <class 'str'> p
        # <class 'str'> body
        # <class 'str'> html
        # <class 'str'> [document]
    
    # Going sideways
    # .next_sibling and .previous_sibling
    link = soup.a
    # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
    print(type(link.next_sibling), link.next_sibling)
    # <class 'bs4.element.NavigableString'>  u',\n'
    print(type(link.next_sibling.next_sibling), link.next_sibling.next_sibling)
    # <class 'bs4.element.Tag'> <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>

    # .next_siblings and .previous_siblings
    for sibling in soup.a.next_siblings:
        print(type(sibling), repr(sibling))     # returns a printable representation
        # <class 'bs4.element.NavigableString'> u',\n'
        # <class 'bs4.element.Tag'> <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
        # <class 'bs4.element.NavigableString'> u' and\n'
        # <class 'bs4.element.Tag'> <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
        # <class 'bs4.element.NavigableString'> u'; and they lived at the bottom of a well.'