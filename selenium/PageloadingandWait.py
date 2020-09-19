from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.page_load_strategy = 'eager'

path = '/Users/sanghunoh/Documents/Develop/chromedriver'
driver = webdriver.Chrome(executable_path=path, options=options)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver.get("https://flight.naver.com/flights/")

# calendar
driver.find_elements(By.XPATH, '//a[@ng-hide]')[2].click()
# start date
driver.find_elements(By.XPATH, '//b[@class="num ng-binding" and .="26"]')[0].click()    # 유효 날짜만 선택 가능
# end date
driver.find_elements(By.XPATH, '//b[@class="num ng-binding" and .="26"]')[1].click()

# arrive
driver.find_elements(By.XPATH, '//dl[@class="recommendation_box"]')[1].click()

# search button
wait_elem = '//a[@class="sp_flight btn_search ng-scope"]'
driver.find_element(By.XPATH, wait_elem).click()

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, wait_elem))
    )
except Exception as e:
    print(e)    
finally:
    driver.quit()