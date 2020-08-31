from django.shortcuts import render,HttpResponse
from background_task import background
# Create your views here.
import time
@background
def task_hello(schedule=3, repeat=10):
    time_tuple = time.localtime()
    time_str = time.strftime("%m/%d/%Y, %H:%M:%S", time_tuple)
    print("task ... Hello World!", time_str)


import requests
from bs4 import BeautifulSoup
import sqlite3
from datetime import datetime

@background
def task_crawling_daum(schedule=60, repeat=60*60*1):
    res = requests.get('http://media.daum.net/economic/')
    links = []
    if res.status_code == 200:
        soup = BeautifulSoup(res.content, 'html.parser')
        links = soup.find_all('a', class_='link_txt')
        # conn = sqlite3.connect('db.sqlite3')
        # query = 'CREATE TABLE economic (crawling_date TEXT, title TEXT, link TEXT, create_date date)'
        # conn.execute(query)
        # conn.commit()
        # conn.close()
        
        date_str = datetime.utcnow().strftime('%Y%m%d')
        time_str = datetime.utcnow().strftime('%Y%m%d%H%M%S%f')
        with sqlite3.connect("db.sqlite3") as con:
            cur = con.cursor()
            title = ''
            link = ''
            query = "INSERT INTO economic (crawling_date, title,link, create_date) VALUES (?,?,?,datetime('now'))"
            for link in links:
                title = str.strip(link.get_text())
                link = link.get('href')
                cur.execute(query,(date_str,title,link))
            con.commit()
    time_tuple = time.localtime()
    time_str = time.strftime("%m/%d/%Y, %H:%M:%S", time_tuple)
    print('task_crawling_daum : ', type(links), len(links), time_str)