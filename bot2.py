from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time
import random
import os

#os.system("/home/gigi/Scrivania/Univers/Projects/facebook-accounts-master/scraper.py")

def slow_typing(value, object):
    for i in value:
        object.send_keys(i)
        time.sleep(random.randint(0, 3)/10)



with open('mails.txt', 'r') as myfile:
    EMAIL_ID = myfile.readline().replace('\n', '')
print(EMAIL_ID)

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("--disable-extensions")
# options.add_argument('disable-infobars')
driver = webdriver.Chrome(options=options,
                          executable_path=r'/home/gigi/Scrivania/Univers/Projects/facebook-accounts-master/chromedriver')
driver.get(
    'https://www.facebook.com/campaign/landing.php?campaign_id=1547344303&extra_1=s%7Cc%7C353835506865%7Ce%7Cfacebook%20register%7C&placement=&creative=353835506865&keyword=facebook%20register&partner_id=googlesem&extra_2=campaignid%3D1547344303%26adgroupid%3D62714189241%26matchtype%3De%26network%3Dg%26source%3Dnotmobile%26search_or_content%3Ds%26device%3Dc%26devicemodel%3D%26adposition%3D1t1%26target%3D%26targetid%3Dkwd-299018535828%26loc_physical_ms%3D1008736%26loc_interest_ms%3D%26feeditemid%3D%26param1%3D%26param2%3D&gclid=EAIaIQobChMIhabO65Px5gIVxuN3Ch1LbAjmEAAYASAAEgLH0PD_BwE')

name = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="u_0_p"]')))

Name = (random.choice(list(open('name.txt'))))

slow_typing(Name, name)

surname = driver.find_element_by_id('u_0_r')
Surname = (random.choice(list(open('cognome.txt'))))

slow_typing(Surname, surname)

# Fill user's email ID
email = driver.find_element_by_id('u_0_u')
slow_typing(EMAIL_ID, email)

email = driver.find_element_by_id('u_0_x')
slow_typing(EMAIL_ID, email)

# Fill user's password
password = driver.find_element_by_id('u_0_z')

# Reads password from a text file
with open('password.txt', 'r') as myfile:
    Password = myfile.read().replace('\n', '')

slow_typing(Password, password)

gender = driver.find_element_by_css_selector("input#u_0_7").click()

select = Select(driver.find_element_by_id('day'))
# select by value
select.select_by_value('1')

select = Select(driver.find_element_by_id('month'))
# select by value
select.select_by_visible_text('apr')

select = Select(driver.find_element_by_id('year'))
# select by value
select.select_by_value('1995')

# click on signup page
signupbutton = driver.find_element_by_id('u_0_16')
signupbutton.click()

time.sleep(1000)

driver.close()
