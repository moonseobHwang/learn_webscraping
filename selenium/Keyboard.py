from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

path = '/Users/sanghunoh/Documents/Develop/chromedriver'
driver = webdriver.Chrome(executable_path=path)
driver.get(url="https://www.google.com/")

# Enter "webdriver" text and perform "ENTER" keyboard action
driver.find_element(By.NAME, "q").send_keys("webdriver" + Keys.ENTER)

SearchInput = driver.find_element(By.NAME, "q")
SearchInput.send_keys("selenium")
# Clears the entered text
SearchInput.clear()

driver.quit()