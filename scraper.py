from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time
import os


options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("--disable-extensions")
# options.add_argument('disable-infobars')
driver = webdriver.Chrome(options=options,
                          executable_path=r'/home/gigi/Scrivania/Univers/Projects/facebook-accounts-master/chromedriver')

driver.get("https://temp-mail.org/en/")
time.sleep(5)
Email = driver.find_element_by_css_selector('#mail')
# content_email = "".join([Email.text() for element in Email])
email = Email.get_attribute("value")
email_content = format(email)
print(email_content)

with open('mails.txt', 'r+') as myfile:
    other = myfile.readlines()
    myfile.seek(0)
    myfile.writelines(email_content+"\n")
    myfile.writelines(other)

time.sleep(5)

driver.close()
