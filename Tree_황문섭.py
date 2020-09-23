from bs4 import BeautifulSoup
import requests, time

base_url = "https://www.google.com/search?q=%EC%B7%A8%EC%97%85%EC%82%AC%EC%9D%B4%ED%8A%B8&ei=KopqX7y0LJKVmAWohI34Ag&start={}&sa=N&ved=2ahUKEwi88YnW9v3rAhWSCqYKHShCAy84HhDy0wN6BAgMEDA&biw=328&bih=927"
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
for n in range (5) :
    url = base_url.format(n*10)
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "lxml")
    a_tags = soup.body
    a_tags = a_tags.select("a > h3")

    for idx, a_tag in enumerate(a_tags):
        print("="*200)
        print("a_tag[{}] page[{}] {} {} ".format(idx+1, n+1, a_tag.get_text(), a_tags[idx].previous_element['href'][7:]))
        time.sleep(1)

# # soup = BeautifulSoup(res.content, features='lxml')
# # link = soup.body
# for n in range (100) :
#     url = base_url.format(n+10)
#     res = requests.get(url=url, headers=header)
#     soup = BeautifulSoup(res.content, 'html.parser')
#     links = soup.select('a')
#     b=0
#     # webpage = urlopen(url)
#     # source = BeautifulSoup(webpage, 'html5lib')
#     # reviews = source.find_all('p', {'class':'desc_review'})
#     # for review in reviews :
#     for link in links:
#         b=b+1
#         if b > 17:    
#             print(type(link),link)      
#             print('-'*100)
#     print(res.status_code, res.content)        
#         # print(review.get_text().strip())


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
