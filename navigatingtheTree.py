from bs4 import BeautifulSoup

with open('datas/sample02.html') as fp:
    soup = BeautifulSoup(fp, features="lxml")
    # Going down - .children
    bodychildren = soup.body.children
    print(type(bodychildren), len(list(bodychildren)))
    # <class 'list_iterator'>
    body_tag = soup.body
    for child in body_tag.children:             #child 사용자 정의 변수
        print(type(child), repr(child))         #returns a printable representation
        # <class 'bs4.element.NavigableSoup'>
        # <class 'bs4.element.Tag><p class="title"><b>....

    # Going up - .parent and .parents
    title_tag = soup.title # <class "bs4.element.Tag"><title>The Dormouse's...</title>
    print(title_tag.parent, title_tag.string.parent)
    link=soup.p
    print(type(link.parents), len(list(link.parents)))

    #a -> p -> body -> html -> document
    print(list(link.parents[0]))
    # <class 'generator'> 4 -generator that behaves like an iterator
    for parent in link.parents:                 #parent 사용자 정의 변수
        print(type(parent.name), parent.name)