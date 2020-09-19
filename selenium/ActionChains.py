from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

path = '/Users/sanghunoh/Documents/Develop/chromedriver'
driver = webdriver.Chrome(executable_path=path)
driver.get(url="https://www.google.com/")
driver.find_element(By.NAME, "q").send_keys("webdriver" + Keys.ENTER)

driver.find_element(By.XPATH, "//body").send_keys(Keys.PAGE_DOWN)

driver.send_keys(Keys.PAGE_DOWN)

driver.find_element(By.XPATH, "//body").send_keys(Keys.PAGE_UP)

# # Perform action ctrl + A (modifier CONTROL + Alphabet A) to select the page
# webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys("a").perform()

# Store google search box WebElement
# search = driver.find_element(By.NAME, "q")
# action = webdriver.ActionChains(driver)
# # Enters text "qwerty" with keyDown SHIFT key and after keyUp SHIFT key (QWERTYqwerty)
# action.key_down(Keys.SHIFT).send_keys_to_element(search, "qwerty")
# .key_up(Keys.SHIFT).send_keys("qwerty").perform()

driver.quit()