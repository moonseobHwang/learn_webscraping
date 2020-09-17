from selenium import webdriver
from selenium.webdriver.common.keys import Keys

path = '/Users/sanghunoh/Documents/Develop/chromedriver'

driver = webdriver.Chrome(path)
driver.get("http://www.python.org")
#if condition returns True, then nothing happens:
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
print(driver.page_source)
import time
time.sleep(90000)   # 9 second
driver.quit()