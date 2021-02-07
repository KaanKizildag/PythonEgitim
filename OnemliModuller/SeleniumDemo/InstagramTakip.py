from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
#####################

class SeleniumController():
    def __init__(self):
        path = os.getcwd()
        self.driver = webdriver.Chrome(
            path + '/chromedriver')
        self.url = 'https://www.instagram.com/?hl=tr'

    def siteyeGit(self):
        self.driver.get(self.url)
        time.sleep(1)

    def girisYap(self,username, password):
        self.siteyeGit()
        tbx = self.driver.find_element_by_css_selector(
            '#loginForm > div > div:nth-child(1) > div > label > input')
        tbx.send_keys(username)

        tbx = self.driver.find_element_by_css_selector(
            '#loginForm > div > div:nth-child(2) > div > label > input')
        tbx.send_keys(password)
        btn = self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]')
        btn.click()

    def kapat(self):
        self.driver.close()

class InstagramBot():
    def __init__(self,controller : SeleniumController):

        self.controller = controller
    def girisYap(self,username, password,):
        self.controller.girisYap(username,password)


controller = SeleniumController()
bot = InstagramBot(controller)

username = input('Kullanıcı adınızı girin: ')
password = input('Şifrenizi girin: ')

bot.girisYap(username,password)

time.sleep(10)
# controller.kapat()