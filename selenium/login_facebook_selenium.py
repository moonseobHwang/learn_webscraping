from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

path = '/Users/sanghunoh/Documents/Develop/chromedriver'
driver = webdriver.Chrome(path)
driver.get("https://www.facebook.com/")
driver.find_element_by_xpath(
    "//input[@id='email']").send_keys("email@domain.com")
driver.find_element_by_xpath("//input[@id='pass']").send_keys("password")
driver.find_element_by_xpath(
    "//input[starts-with(@id, 'u_0_')][@value='Log In']").click()
print(driver.title)
WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
    (By.XPATH, "//div[starts-with(@id, 'u_0_')]//textarea[@name='xhpc_message']")))
driver.find_element_by_xpath(
    "//div[starts-with(@id, 'u_0_')]//textarea[@name='xhpc_message']").send_keys("Hie")
print("Typed Hie within Facebook Status Box")
