from bs4 import BeautifulSoup
import csv

path_in = 'datas/sample01.html'
soup = BeautifulSoup(open(path_in), features="lxml")

final_link = soup.a
# final_link.decompose()

path_out = 'datas/output01.csv'

links = soup.find_all('a')

f = csv.writer(open(path_out, "w"))
f.writerow(["Name", "Link"])    # Write column headers as the first line

for link in links:
    names = link.contents[0]
    fullLink = link.get('href')

    f.writerow([names,fullLink])