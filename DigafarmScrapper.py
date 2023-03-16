import time

import mysql.connector
import pandas as pd
import regex as re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="hbits"
)
mycursor=mydb.cursor()


options = Options()
prefs = {
  "translate_whitelists": {"de":"en"},
  "translate":{"enabled":"true"}
}
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome("C:/Users/devanjan.mukherjee/Downloads/chromedriver_win32/chromedriver.exe", options=options)


URL="https://diga.bfarm.de/de/verzeichnis/"

driver.get(URL)
time.sleep(30)
driver.maximize_window()

filter_closed = driver.find_elements(By.CLASS_NAME, 'app-filter__content')[0].find_element(By.TAG_NAME, 'i')
filter_closed.click()
print("filters closed")
time.sleep(10)

# appbox = driver.find_elements(By.CLASS_NAME, "entity-app.")
# print(len(appbox))
soup = BeautifulSoup(driver.page_source, 'html.parser')
# print(soup.prettify())
links = soup.findAll("div", class_=re.compile(r'^entity-app$'))
print(len(links))
for i in range(len(links)):
  # print(links[i].text.strip())
  print("AppName")
  AppName=links[i].find('div', class_='entity-app__header__name').text.strip()
  print(AppName)
  print("Platforms")
  Platforms=links[i].find('div', class_='entity-app__info__list__items').text.strip().replace('\n',', ').replace('                 , , , , ,                     ',' ')
  print(Platforms)
  print("App Diga Farm url")
  AppURL='https://diga.bfarm.de'+links[i].find('a', class_='ember-view entity-app__button')['href']
  print(AppURL)
  print('App Logo')
  AppLogo=links[i].find('img', class_='image-app__image')['src']
  print(AppLogo)
  print('\n\n')
  vals = (AppName, AppLogo, AppURL)
  sql = ("""Insert into sys.tbldigafarm(AppName, AppLogo, AppURL) Values (%s,%s,%s)""")
  mycursor.execute(sql,vals)
  mydb.commit()
  Platforms=Platforms.split(', ')
  print(Platforms)
  appID= pd.read_sql("""Select ID from sys.tbldigafarm WHERE AppName="%s";""" % AppName, mydb)
  print(appID['ID'][0])
  # print(len(appID))
  for j in Platforms:
    vals3=(j, int(appID['ID'][0]))
    sql3=("""Insert into sys.tbldigafarmplatforms(Platform, digafarmID) Values (%s,%s)""")
    mycursor.execute(sql3,vals3)
    mydb.commit()



