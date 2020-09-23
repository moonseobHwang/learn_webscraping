from bs4 import BeautifulSoup
import sqlite3,requests, bs4

url = "http://www.jobkorea.co.kr/user/mypage"
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
res = requests.get(url)    
soup = BeautifulSoup(res.text, "lxml")
soup = soup.section

links = soup.select('div > a')

    # with sqlite3.connect("db.sqlite3") as con:
    #     cur = con.cursor()
    #     query="INSERT INTO sample03(title,link,create_date) Values (?, ?, datetime('now'))"
        
for link in links:
    title=str.strip(link.get_text())
    link = link['a']
    #     cur.execute(query,(title,link))
    # con.commit()