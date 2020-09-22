from bs4 import BeautifulSoup

with open('datas/sample02.html') as fp:
    soup = BeautifulSoup(fp, features="lxml")

    print(type(soup.find(id="link3")), soup.find(id="link3"))
    
    print(type(soup.find_all(name='a')),soup.find_all(name='a'))

    print(type(soup.find_all(name='b')),soup.find_all(name='b'))

    print(type(soup.find_all(name=['a','b'])),soup.find_all(name=['a','b']))

    print(type(soup.find_all(id=True)),soup.find_all(id=True))

    find_attrs=soup.find_all(name='a',attrs={"href":True})
    print(type(find_attrs), find_attrs)

    find_attrs=soup.find_all(name='a', attrs={"class":'sister', 'id':['link2','link3']})
    print(type(find_attrs), find_attrs)