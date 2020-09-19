from selenium import webdriver

path = '/Users/sanghunoh/Documents/Develop/chromedriver'
driver = webdriver.Chrome(executable_path=path)
print(type(driver), driver)
#<class 'selenium.webdriver.chrome.webdriver.WebDriver'> <selenium.webdriver.chrome.webdriver.WebDriver (session="224a1f7cadb8a9d0b2d338ccc40ab4cc")>

driver.get(url="https://www.google.com/")
print(type(driver.page_source), driver.page_source)
# <class 'str'> '<html itemscope=""  ... </body></html>'

# import time
# time.sleep(900)   # 9 second
driver.quit()