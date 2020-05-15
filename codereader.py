from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

def slow_typing(value, object):
    for i in value:
        object.send_keys(i)
        time.sleep(random.randint(0, 3)/10)

def takeMail():
    drivermail.get("https://temp-mail.org/en/")
    time.sleep(10)
    Email = drivermail.find_element_by_css_selector('#mail')
    # content_email = "".join([Email.text() for element in Email])
    email = Email.get_attribute("value")
    email_content = format(email)
    print(email_content)

    with open('mails.txt', 'r+') as myfile:
        other = myfile.readlines()
        myfile.seek(0)
        myfile.writelines(email_content + "\n")
        myfile.writelines(other)

def createAccount():
    with open('mails.txt', 'r') as myfile:
        EMAIL_ID = myfile.readline().replace('\n', '')
    print(EMAIL_ID)

    driverfb.get('https://www.facebook.com/')

    name = WebDriverWait(driverfb, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="u_0_o"]')))

    Name = (random.choice(list(open('name.txt'))))

    slow_typing(Name, name)

    surname = driverfb.find_element_by_id('u_0_q')
    Surname = (random.choice(list(open('cognome.txt'))))

    slow_typing(Surname, surname)

    # Fill user's email ID
    email = driverfb.find_element_by_id('u_0_t')
    slow_typing(EMAIL_ID, email)

    email = driverfb.find_element_by_id('u_0_w')
    slow_typing(EMAIL_ID, email)

    # Fill user's password
    password = driverfb.find_element_by_id('u_0_y')

    # Reads password from a text file
    with open('password.txt', 'r') as myfile:
        Password = myfile.read().replace('\n', '')

    slow_typing(Password, password)

    gender = driverfb.find_element_by_css_selector("input#u_0_7").click()

    select = Select(driverfb.find_element_by_id('day'))
    # select by value
    select.select_by_value('1')

    select = Select(driverfb.find_element_by_id('month'))
    # select by value
    select.select_by_visible_text('apr')

    select = Select(driverfb.find_element_by_id('year'))
    # select by value
    select.select_by_value('1995')

    # click on signup page
    signupbutton = driverfb.find_element_by_id('u_0_15')
    signupbutton.click()

#main

PROXY = "200.89.178.219:80" # IP:PORT or HOST:PORT
options = webdriver.ChromeOptions()
options.add_argument('--proxy-server=%s' % PROXY)
options.add_argument("start-maximized")
options.add_argument("--disable-extensions")

# options.add_argument('disable-infobars')
driverfb = webdriver.Chrome(options=options,
                          executable_path=r'/home/gigi/Scrivania/Univers/Projects/facebook-accounts-master/chromedriver')

# options.add_argument('disable-infobars')
drivermail = webdriver.Chrome(options=options,
                          executable_path=r'/home/gigi/Scrivania/Univers/Projects/facebook-accounts-master/chromedriver')

def writeCode():
    with open('codes.txt', 'r') as myfile:
        codeid = myfile.readline().replace('\n', '')

takeMail()
createAccount()