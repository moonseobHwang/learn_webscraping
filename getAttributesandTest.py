from bs4 import BeautifulSoup
import requests, bs4

with open('datas/sample03.html',encoding='UTF8') as fp:
    soup=BeautifulSoup(fp, features='lxml')
    title_data=soup.find('h1')
    print(type(title_data), title_data, title_data.string)
    # <class 'bs4.element.Tag'> <h1 class="public_class_name" id="h1_id_name">[1]크롤링이란?</h1> [1]크롤링이란?

    title_data=soup.find_all(id='h1_id_name')
    print(title_data, title_data[0].get_text())
    # [<h1 class="public_class_name" id="h1_id_name">[1]크롤링이란?</h1>] [1]크롤링이란?
    
    title_data=soup.find_all('p', class_="public_class_name")
    print(title_data,title_data[0].attrs)
    # [<p class="public_class_name" id="p01_id_name">웹페이지...것</p>] {'class': ['public_class_name'], 'id': 'p01_id_name'}

    title_data=soup.find_all('p',id='p02_id_name')
    print(title_data,title_data[0].string)
    
    title_data=soup.find_all('a',href=True)
    print(title_data, title_data[0].string)