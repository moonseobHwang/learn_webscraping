from selenium import webdriver
from selenium.webdriver.common.by import By

path = '/Users/sanghunoh/Documents/Develop/chromedriver'

driver = webdriver.Chrome(executable_path=path)
# print(type(driver), driver)
#<class 'selenium.webdriver.chrome.webdriver.WebDriver'> <selenium.webdriver.chrome.webdriver.WebDriver (session="224a1f7cadb8a9d0b2d338ccc40ab4cc")>
driver.get(url="https://www.google.com/")

# Get search box element from webElement 'q' using Find Element
search_form = driver.find_element(By.TAG_NAME, "form")
print(type(search_form), search_form)
# <class 'selenium.webdriver.remote.webelement.WebElement'> <selenium.webdriver.remote.webelement.WebElement (session="8ae6c623be132d96abde5003a982ea0c", element="be89ca22-0a85-4b36-96d6-ccc3bb613941")>

# Find Element From Element
search_box = search_form.find_element(By.NAME, "q")
search_box.send_keys("webdriver")    
print(type(search_box), search_box)
# <class 'selenium.webdriver.remote.webelement.WebElement'> <selenium.webdriver.remote.webelement.WebElement (session="6405eeb381591e4c2e38ffd87eb15db1", element="d973ad8f-b71a-4c9c-8d0c-efeb4546be2f")>

# Is Element Enabled
# Returns true if element is enabled else returns false
# driver.implicitly_wait(10)
result_element = driver.find_element(By.NAME, 'btnK')
result_element.screenshot('datas/screenshot.png')       # need break point
value = result_element.is_enabled()
print(type(value), value)
# <class 'bool'> True

# Is Element Selected
# Navigate to url
driver.get("https://the-internet.herokuapp.com/checkboxes")
# Returns true if element is checked else returns false
# value = driver.find_element(By.CSS_SELECTOR, "input[type='checkbox']:first-of-type").is_selected()
value = driver.find_element(By.CSS_SELECTOR, "input[type='checkbox']").is_selected()
print(type(value), value)
# <class 'bool'> False

# Get Element TagName
attr = driver.find_element(By.CSS_SELECTOR, "[name='viewport']").tag_name
print(type(attr), attr)
# <class 'str'> meta

driver.get(url="https://www.google.com/")
# Get Element Rect
res = driver.find_element(By.CSS_SELECTOR, 'input[name="q"]').rect
print(type(res), res)
# <class 'dict'> {'height': 34, 'width': 298, 'x': 128.5, 'y': 280.5}

# Find Element From Elements
driver.get(url="https://www.google.net/search?q=webdriver")
elements = driver.find_elements(By.XPATH, '//a[@href]')
print(type(elements), elements)
# <class 'list'> [<selenium.webdriver. ..., -8638-2f7617332c69")>]
for e in elements:
    if e != None:
        print(type(e.text), repr(e.text))
        # <class 'str'> <a ...
        # <class 'str'> <a ...

# import time
# time.sleep(900)   # 9 second
driver.quit()