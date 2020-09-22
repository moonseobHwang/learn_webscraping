from bs4 import BeautifulSoup
import requests

url = "https://www.google.com/search?q=%EC%B7%A8%EC%97%85%EC%82%AC%EC%9D%B4%ED%8A%B8&oq=%EC%B7%A8%EC%97%85%EC%82%AC%EC%9D%B4%ED%8A%B8&aqs=chrome..69i57.2150j0j15&sourceid=chrome&ie=UTF-8"
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
res = requests.get(url=url, headers=header)
soup = BeautifulSoup(res.content, 'html.parser')
links = soup.select('a')
b=0
for link in links:
    b=b+1
    if b > 100:    
        print(type(link),link)      
        print('-'*100)
#print(res.status_code, res.content)
# soup = BeautifulSoup(res.content, features='lxml')
# link = soup.body
# print(type(link), link.a.next_siblings)
# for sibling in link.children:
#     for sibling2 in sibling.div.next_siblings:
#         print(sibling2)
#     for sibling2 in link.div.next_siblings:
#         if link.a.next_siblings== True:
#             for sibling3 in link.a.next_siblings:
#                 print(type(sibling3), list(sibling3), sibling3)

# while link.a.next_siblings == False:
#     tmp = link.a.next_siblings
#     print(tmp)

# with open('datas/sample02.html') as fp:
#     soup = BeautifulSoup(fp, features="lxml")



#     link = soup.a
#     print(type(link.next_sibling),link.next_sibling)
#     print(type(link.next_sibling.next_sibling),link.next_sibling.next_sibling)

#     for sibling in soup.a.next_siblings:
#         print(type(sibling), repr(sibling))
