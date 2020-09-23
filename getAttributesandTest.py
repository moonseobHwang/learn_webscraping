from bs4 import BeautifulSoup
import requests

with open('datas/sample03.html') as fp:
    soup = BeautifulSoup(fp, features='lxml')
    title_data=soup.find('h1')
    print(type(title_data), title_data, title_data.string)
    title_data=soup.find_all(id='h1_id_name')
    print(title_data, title_data[0].get_text())
    title_data=soup.find_all('p', class_="public_class_name")
    print(title_data,title_data[0].attrs)
    title_data=soup.find_all('p',attr={'align':'center'})
    print(title_data,title_data[0].string)
    title_data=soup.find_all('a',href=True)
    print(title_data, title_data[0].string)