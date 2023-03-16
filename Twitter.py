import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome("C:/Users/devanjan.mukherjee/Downloads/chromedriver_win32/chromedriver.exe")
driver.maximize_window()
driver.get('https://twitter.com/i/flow/login')
time.sleep(10)
actions = ActionChains(driver)
#
username = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')

actions.move_to_element(username).perform()
time.sleep(10)
username.send_keys('devanjan.mukherjee@humanebits.com')
time.sleep(5)
print("username inserted")
#
NextElement=driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span')
actions.move_to_element(NextElement).perform()
NextElement.click()
time.sleep(3)
try:
    x=driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
    x.send_keys('DevanjanHBITS')
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/span/span').click()
    time.sleep(10)
except NoSuchElementException:
    print(1)

time.sleep(20)
password=driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
actions.move_to_element(password).perform()
password.send_keys('Devanjan@HBITS')
print('password inserted')
time.sleep(5)

Login=driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/div/span')
actions.move_to_element(Login).perform()
Login.click()
print('Logged in')
time.sleep(10)
# data = {"session[username_or_email]":"devanjan.mukherjee@hbits.com",
#     "session[password]":"Devanjan@HBITS"}
# r = requests.post("https://twitter.com/login/", data=data)
#
# print(r)
