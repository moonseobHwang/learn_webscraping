from bs4 import BeautifulSoup
import requests, sqlite3

url = "https://www.google.com/search?q=%EC%B7%A8%EC%97%85%EC%82%AC%EC%9D%B4%ED%8A%B8&ei=KopqX7y0LJKVmAWohI34Ag&start=0&sa=N&ved=2ahUKEwi88YnW9v3rAhWSCqYKHShCAy84HhDy0wN6BAgMEDA&biw=328&bih=927"
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}

res = requests.get(url)
soup = BeautifulSoup(res.text, "lxml")
a_tags = soup.body
a_tags = a_tags.select("a > h3")
with sqlite3.connect("db.sqlite3") as con:
    cur = con.cursor()
    query="INSERT INTO sample03(title,link,create_date) Values (?, ?, datetime('now'))"

    for idx, a_tag in enumerate(a_tags):
        title = str.strip(a_tag.get_text())
        link = a_tags[idx].previous_element['href'][7:]
        cur.execute(query,(title,link)
    con.commit()