from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome("C:/Users/devanjan.mukherjee/Downloads/chromedriver_win32/chromedriver.exe")
driver.maximize_window()
driver.get('https://www.linkedin.com/home')
time.sleep(5)
actions = ActionChains(driver)
textfields=driver.find_elements(By.CLASS_NAME, "text-color-text.font-sans.text-md.outline-0.bg-color-transparent.grow")

username=textfields[0]
password=textfields[1]
actions.move_to_element(username).perform()
time.sleep(2)
username.send_keys('devanjan.mukherjee@humanebits.com')
actions.move_to_element(password).perform()
time.sleep(2)
password.send_keys('Devanjan@HBITS')
time.sleep(5)
Signin = driver.find_element(By.CLASS_NAME, 'btn-md.btn-primary.flex-shrink-0.cursor-pointer.sign-in-form__submit-btn--full-width')
actions.move_to_element(Signin).perform()
time.sleep(2)
Signin.click()

time.sleep(30)

