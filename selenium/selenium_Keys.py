from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

import json
import os
import argparse

import requests
# import urllib
# import urllib3
# from urllib3.exceptions import InsecureRequestWarning

import datetime
import time

# urllib3.disable_warnings(InsecureRequestWarning)

searchword1 = 'cat'
searchword2 = 'dog'
searchword3 = 'cartoon'

searchurl = 'https://www.google.com/search?q=' + searchword1 + '+' + searchword2 + '+' + searchword3 + '&source=lnms&tbm=isch'
dirs = 'pictures' 
maxcount = 1000

chromedriver = '/Users/sanghunoh/Documents/Develop/chromedriver'

import sys
if not os.path.exists(dirs):
    os.mkdir(dirs)

def download_google_staticimages():

    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    #options.add_argument('--headless')

    try:
        browser = webdriver.Chrome(chromedriver, options=options)
    except Exception as e:
        print(f'No found chromedriver in this environment.')
        print(f'Install on your machine. exception: {e}')
        sys.exit()

    browser.set_window_size(1280, 1024)
    browser.get(searchurl)
    time.sleep(1)

    print(f'Getting you a lot of images. This may take a few moments...')

    element = browser.find_element_by_tag_name('body')

    # Scroll down
    #for i in range(30):
    for i in range(50):
        element.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.3)

    try:
        browser.find_element_by_id('smb').click()
        for i in range(50):
            element.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.3)
    except:
        for i in range(10):
            element.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.3)

    print(f'Reached end of page.')
    time.sleep(0.5)
    print(f'Retry')
    time.sleep(0.5)

    # Below is in japanese "show more result" sentences. Change this word to your lanaguage if you require.
    searchword = searchword1 +' '+searchword2+' '+searchword3
    browser.find_element_by_xpath('//input[@value="cat dog cartoon"]').click()

    browser.close()
    return i

# Main block
def main():
    t0 = time.time()
    count = download_google_staticimages()
    t1 = time.time()

    total_time = t1 - t0
    print(f'\n')
    print(f'Download completed. [Successful count = {count}].')
    print(f'Total time is {str(total_time)} seconds.')

if __name__ == '__main__':
    main()