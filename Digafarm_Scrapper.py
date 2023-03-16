import mysql.connector
import requests
from datetime import datetime, timezone
from bs4 import BeautifulSoup
import os
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.common.exceptions import ElementClickInterceptedException

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="hbits"
)
mycursor=mydb.cursor()

URL="https://diga.bfarm.de/de/verzeichnis/"
head = {"Accept-Language": "en,en-gb;q=0.5"}
options = Options()
prefs = {
  "translate_whitelists": {"de":"en"},
  "translate":{"enabled":"true"}
}
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
PARAMS = {'header':head}
driver.get(URL)
time.sleep(30)

filter_closed = driver.find_elements(By.CLASS_NAME, 'app-filter__content')[0].find_element(By.TAG_NAME, 'i')
filter_closed.click()
print("filters closed")
time.sleep(10)


# req = requests.get(URL, headers=headers)
# # print(req.content)
# soup = BeautifulSoup(req.content, 'html5lib')
# # print(soup.prettify())
#
# applications=soup.findAll("div", {"class":"app-main-columns__content"})


# print(soup.text)

# print(driver.find_element(By.XPATH, "/html/body").text)

all_apps = driver.find_elements(By.CLASS_NAME, "entity-app__header")
platforms=driver.find_elements(By.CLASS_NAME, "entity-app__info__list__items")
logo=driver.find_elements(By.CLASS_NAME, 'image-app__image')
url=driver.find_elements(By.CSS_SELECTOR, '.ember-view.entity-app__button')
# print(len(url))

for i in range(10,len(all_apps)):
  app_name = all_apps[i].find_element(By.CLASS_NAME, "entity-app__header__name").text.strip()
  print(app_name)
  pln = i*3
  app_platforms = platforms[pln].text.strip().replace('\n',', ')
  print(app_platforms)
  app_logo= logo[i].get_attribute("src")
  print(app_logo)
  app_url=url[i].get_attribute("href")
  print(app_url)

  vals=(app_name, app_platforms, app_logo, app_url, datetime.now())
  sql=("""Insert into sys.diga_bfarm(Application_Name, Application_Platforms, Application_Logo, Application_Diga_Bfarm_URL, Timestamp)
         Values (%s,%s,%s,%s,%s)""")
  mycursor.execute(sql, vals)
  mydb.commit()
  print('\n')

  entity - app

  entity - app - -mobile



