from tbselenium.tbdriver import TorBrowserDriver
from os.path import dirname, join, realpath, getsize
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("--disable-extensions")

# options.add_argument('disable-infobars')
drivermail = webdriver.Chrome(options=options,
                          executable_path=r'/home/gigi/Scrivania/Univers/Projects/facebook-accounts-master/chromedriver')

drivermail.get("https://temp-mail.org/en/")

time.sleep(60)

message = drivermail.find_element_by_css_selector('body > main > div.container > div > div.col-sm-12.col-md-12.col-lg-12.col-xl-8 > div.tm-content > div > div.inboxWarpMain > div > div.inbox-dataList > ul > li:nth-child(2) > div.col-box.hidden-xs-sm > span > a').click()




body > main > div.container > div > div.col-sm-12.col-md-12.col-lg-12.col-xl-8 > div.tm-content > div > div.inboxWarpMain > div > div.inbox-data-content > div.inbox-data-content-intro > div