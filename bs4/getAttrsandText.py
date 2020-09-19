from bs4 import BeautifulSoup

# from file
path = 'datas/sample02.html'
with open(path) as fp:
    soup = BeautifulSoup(fp, features='lxml')
    print(type(soup), soup.attrs, soup.getText())
    # <class 'bs4.BeautifulSoup'> {} The Dormouse's story ...

    elements = soup.findAll(name='a')
    print(type(elements), len(list(elements)))
    # <class 'bs4.element.ResultSet'> 3
    for element in elements:
        print(type(element), element.attrs, element['href'])
        print(element.getText(), len(element.getText()))    # need trip()
        # <class 'bs4.element.Tag'> {'class': ['sister']...} http://example01.com/elsie Elsie 14
        # ...
        
    body_tag = soup.body
    bodychildren = body_tag.children
    print(type(bodychildren), len(list(bodychildren)))
    # <class 'list_iterator'> 7
    
    from bs4.element import NavigableString
    for child in body_tag.children:
        if isinstance(child, NavigableString):
            print(type(child), repr(child.string), len(child.string))
        else:
            print(type(child), child.attrs, child.getText(), len(child.getText()))
            # <class 'bs4.element.NavigableString'> '\n' 1
            # <class 'bs4.element.Tag'> {'class': ['title']} 
            # The Dormouse's story
            # ...
            # <class 'bs4.element.NavigableString'>