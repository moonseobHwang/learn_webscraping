from selenium import webdriver
path = '/Users/sanghunoh/Documents/Develop/chromedriver'
options = webdriver.ChromeOptions()
# options.headless = True
options.add_argument("user-agent=whatever you want")
options.add_argument('--window-size=1920,1080')

driver = webdriver.Chrome(executable_path=path,chrome_options=options)
driver.get('https://www.google.com/')
print(driver.page_source)
driver.close()      # Tab
