from selenium import webdriver

path = '/Users/sanghunoh/Documents/Develop/chromedriver'

driver = webdriver.Chrome(executable_path=path)
# print(type(driver), driver)
#<class 'selenium.webdriver.chrome.webdriver.WebDriver'> <selenium.webdriver.chrome.webdriver.WebDriver (session="224a1f7cadb8a9d0b2d338ccc40ab4cc")>

# get the image source
from selenium.webdriver.common.by import By
import wget
import urllib.request

# As HTTP 200
url='https://www.coupang.com/np/search?q=컴퓨터'  
driver.get(url=url)
elements = driver.find_elements(By.XPATH, '//img[@class="search-product-wrap-img"]')
down_path = 'pictures/'

for element in elements:
    src = element.get_attribute('src')
    # download the image
    img_txt = src.split('/')[-1]
    image_name = down_path+img_txt

    # first way
    # wget.download(url=src, out=image_name)  # HTTP Error 403: Forbidden

    # second way
    # Download the file from `url` and save it locally under `file_name`:
    with urllib.request.urlopen(src) as response, open(image_name, 'wb') as out_file:
        data = response.read() # a `bytes` object
        out_file.write(data)

# src url As HTTP Error 403: Forbidden
url='https://intellipaat.com/'  
driver.get(url=url)
elements = driver.find_elements(By.XPATH, '//a/img[@src and @alt]')
down_path = 'pictures/'
for element in elements:
    src = element.get_attribute('src')
    # download the image
    img_txt = element.get_attribute('alt')
    if img_txt is not None:
        image_name = down_path+img_txt+".png"
        # As HTTP Error 403: Forbidden
        element.screenshot(image_name)

# import time
# time.sleep(900)   # 9 second
driver.quit()