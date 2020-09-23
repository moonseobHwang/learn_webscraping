from bs4 import BeautifulSoup
import requests, bs4
import pandas as pd

wikipage = "https://en.wikipedia.org/wiki/List_of_sovereign_states_and_dependent_territories_by_continent_(data_file)"
result=requests.get(wikipage)
if result.status_code == 200:
    soup = BeautifulSoup(result.content,"lxml")
table = soup.find('table',{'class':'wikitable sortable'})
new_table=[]
for row in table.find_all("tr")[1:]:
    colunms = row.find_all('td')
    new_table.append([colunms.get_text() for colunms in colunms])
df = pd.DataFrame(new_table, columns=['ContinentCode','Alpha2','Alpha3','PhoneCode','Name'])
