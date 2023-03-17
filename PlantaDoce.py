import time
import dateparser
import mysql.connector
import pandas as pd
import regex as re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import requests

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="hbits"
)
mycursor = mydb.cursor()

def PlantaDoce(SearchWord):
    URL = "https://www.plantadoce.com/buscar.html?search_text="+SearchWord
    req = requests.get(URL)
    soup=BeautifulSoup(req.content, 'html5lib')
    # print(soup.prettify())
    print(req)
    articles= soup.findAll("article", class_="news_list_item")
    print(len(articles))
    ArticlesList=[]
    for each_article in articles:
        title=each_article.find("div", class_="maintext").find('div', class_='title')
        Title=title.text
        print(Title)
        TitleURL=URL[:-1]+title.find("a")['href']
        print(TitleURL)
        TitleSummary=each_article.find("div", class_="maintext").find('div', class_='text').text.rstrip().strip()
        print(TitleSummary)
        Date=each_article.find("div", class_="datetime").text.split(' — ')
        print(Date)
        ArticleDate=dateparser.parse(Date[0])
        day = ArticleDate.day
        month = ArticleDate.month
        year = ArticleDate.year
        time=Date[1]
        vals=(Title, TitleSummary, TitleURL, day, month, year, time,'PlantaDoce')
        print(vals)
        ArticlesList.append(vals)

    return ArticlesList

if __name__=="__main__":
    SearchWord='Diabetes'
    x=PlantaDoce(SearchWord)
    print(x)
