from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

path = '/Users/sanghunoh/Documents/Develop/chromedriver'
driver = webdriver.Chrome(executable_path=path)
print(type(driver), driver)
#<class 'selenium.webdriver.chrome.webdriver.WebDriver'> <selenium.webdriver.chrome.webdriver.WebDriver (session="224a1f7cadb8a9d0b2d338ccc40ab4cc")>

driver.get(url="https://www.google.co.kr/imghp")
driver.find_element(By.NAME, 'q').send_keys('drone' + Keys.ENTER)

scroll_height = driver.execute_script('return document.body.scrollHeight')
stop_flag = 1
routine = 1
import time
while stop_flag:
    driver.execute_script('window.scrollTo(0, '+str(scroll_height)+')')
    time.sleep(3)
    
    current_height = driver.execute_script('return document.body.scrollHeight')
    if scroll_height == current_height:
        if routine > 0:
            driver.find_element(By.XPATH, '//input[@jsaction="Pmjnye"]').send_keys(Keys.ENTER)
        else :
            stop_flag = 0
        routine =- 1
    
    scroll_height = current_height


# print(type(driver.page_source), driver.page_source)
# <class 'str'> '<html itemscope=""  ... </body></html>'
# import time
# time.sleep(900)   # 9 second
driver.quit()