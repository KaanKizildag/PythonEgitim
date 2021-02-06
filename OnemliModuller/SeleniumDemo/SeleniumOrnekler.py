from selenium import webdriver
import os
import time
path = os.getcwd()

driver = webdriver.Chrome(path + '/chromedriver')

driver.get('https://github.com/')
time.sleep(1)
print(driver.title)

driver.save_screenshot('github_ekran.png')

url = 'https://paste.ubuntu.com/'
driver.get(url)
time.sleep(1)

driver.back()
# driver.forward()
time.sleep(1)

driver.close()