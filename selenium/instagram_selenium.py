import sys
# import os
# sys.path.append(os.getcwd()+"/ownconfiguration")

from ownconfiguration.readconfig import *
username = getConfigElement('email01')
userpw = getConfigElement('password01')

import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument('--disable-dev-shm-usage')
# chrome_options.add_argument('--headless')

path = "/Users/sanghunoh/Documents/Develop/chromedriver"
driver = webdriver.Chrome(path, chrome_options=chrome_options)
loginUrl = 'https://www.instagram.com/accounts/login/?next=%2Fofficial_sunmi%2F&source=desktop_nav'
driver.get(loginUrl)
driver.implicitly_wait(5)

# 로그인
username = 'mahau.master@gmail.com'
userpw = 'my passwd'
driver.find_element_by_name('username').send_keys(username)
driver.find_element_by_name('password').send_keys(userpw)
driver.implicitly_wait(5)

driver.find_element_by_xpath('//button[@type="submit"]').submit()
driver.implicitly_wait(5)

driver.find_element_by_xpath('//button[@type="button" and .="Not Now"]').click()
driver.implicitly_wait(5)

# 첫번째 게시물
def select_first(driver):
   first = driver.find_element_by_css_selector('body > div#react-root > section > main > div > div._2z6nI > article > div:nth-child(1) > div > div:nth-child(1) > div:nth-child(1) > a')
   first.click()
   time.sleep(3)

select_first(driver)

# 댓글 크롤링
source = driver.page_source
soup = BeautifulSoup(source, 'lxml')
links = soup.find_all('div',class_='C4VMK')

reply=str()
for link in links:
   for replys in link.find_all('span'):
       reply = str.strip(replys.get_text())
       print(reply)
