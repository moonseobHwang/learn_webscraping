from selenium import webdriver
from selenium.webdriver.common.by import By

path = '/Users/sanghunoh/Documents/Develop/chromedriver'

driver = webdriver.Chrome(executable_path=path)
# print(type(driver), driver)
#<class 'selenium.webdriver.chrome.webdriver.WebDriver'> <selenium.webdriver.chrome.webdriver.WebDriver (session="224a1f7cadb8a9d0b2d338ccc40ab4cc")>
driver.get(url="https://www.google.com/")

# Get Active Element
webelement = driver.find_element(By.CSS_SELECTOR, '[name="q"]')
# Get attribute of current active element
attr = driver.switch_to.active_element.get_attribute("title")
print(type(attr), attr)
# <class 'str'> 검색

# Gets the given attribute or property of the element
attr = webelement.get_attribute("title")
print(type(attr), attr)
# <class 'str'> 검색
value = webelement.get_attribute("value")
print(type(value), repr(value))
# <class 'str'> ''
webelement.send_keys("webElement")
value = webelement.get_attribute("value")
print(type(value), repr(value))
# <class 'str'> webElement

webelement = driver.find_element(By.CSS_SELECTOR, 'a')
print(type(webelement.text), webelement.text)
# <class 'str'> Gmail
# import time
# time.sleep(900)   # 9 second
driver.quit()