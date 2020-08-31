from selenium import webdriver
from selenium.webdriver.common.by import By

path = '/Users/sanghunoh/Documents/Develop/chromedriver'
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')
# driver = webdriver.Chrome(path,chrome_options=chrome_options)
driver = webdriver.Chrome(path)

# login
driver.get('http://sdacademy.maniaro.com/')
driver.implicitly_wait(5)
username = 'my_id'
userpw = 'my_password'
driver.find_element_by_name('strUid').send_keys(username)
driver.find_element_by_name('strPassword').send_keys(userpw)
driver.find_element_by_xpath("//input[@type='submit']").click()
driver.implicitly_wait(5)

# home
print(driver.page_source)
driver.quit()