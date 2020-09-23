from bs4 import BeautifulSoup
import requests, bs4

url = "https://www.naver.com/"
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
a = {"FINANCE"}
res = requests.get(url)
soup = BeautifulSoup(res.content, "lxml")
body_data = soup.body
body_data = body_data.select("div", data_panel_code="FINANCE")

for s_data in body_data:

    print("-"*100)
    print(s_data.get_text(), s_data.previous_element, s_data.find("div", class_="group_theme"))