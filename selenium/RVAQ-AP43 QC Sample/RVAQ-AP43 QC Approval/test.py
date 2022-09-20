import datetime
from time import sleep, time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 1. open browser via chromedriver.exe
browser = webdriver.Chrome(r'.\chromedriver.exe')
n = datetime.datetime.now()
webSiteSuccess = False


# 2. go to website.
while True:
    c = datetime.datetime.now() - n
    browser.get(r'http://192.168.102.4/fldb/')
    webSiteSuccess = (browser.title.upper() == 'FORTINET FLOOR CONTROL SYSTEM')

    if webSiteSuccess:
        print('================website open success================')
        break

    if c.seconds >= 5:
        print('website open fail...timeout...')
        break

    sleep(1)

# 3. wait until some element show to judge the website open success.
if webSiteSuccess:
    try:
        ele_login_btn_show = WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.ID, 'ext-gen23')))
        ele_username = browser.find_element(by=By.ID, value='ext-comp-1002').send_keys('Ellie.Sun@wnc.com.tw')
        ele_password = browser.find_element(by=By.ID, value='ext-comp-1004').send_keys('Aa111222')
        ele_login_btn = browser.find_element(by=By.ID, value='ext-gen23').click()
    except:
        raise


browser.close()
