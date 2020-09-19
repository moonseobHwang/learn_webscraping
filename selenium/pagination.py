from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

path = '/Users/sanghunoh/Documents/Develop/chromedriver'

driver = webdriver.Chrome(executable_path=path)
path = "https://www.k-startup.go.kr/common/announcement/announcementList.do?mid=30004&bid=701&searchAppAt=N&searchModeKeword=A"
driver.get(url=path)

current_page = 10
import time
while True:
    try:
        next_page_link = driver.find_element(By.XPATH, '//a[contains(@onclick,"goPage('+str(current_page)+')")]')
        next_page_link.click()
        current_page = current_page + 1
    except NoSuchElementException:
        print("Exiting. Last page: {}.",current_page)
        break
    time.sleep(3)
driver.quit()
