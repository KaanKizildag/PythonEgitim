from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time
url = 'https://github.com/explore'
path = os.getcwd()
driver = webdriver.Chrome(path + '/chromedriver')

driver.get(url)

tbxInput = \
    driver.find_element_by_xpath(
        '/html/body/div[1]/header/div/div[2]/div[2]/div/div/div/form/label/input[1]')

tbxInput.send_keys('python')
tbxInput.send_keys(Keys.ENTER)
source = driver.page_source
print(source)
time.sleep(3)
driver.close()