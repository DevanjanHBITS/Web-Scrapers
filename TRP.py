import dateparser as dateparser
import mysql.connector
import requests
from datetime import datetime, timezone
from bs4 import BeautifulSoup

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="hbits"
)
mycursor = mydb.cursor()


# URL="https://www.therakyatpost.com/?s=BIO"

def TRP_scrapper(SearchWord):
    URL = "https://www.therakyatpost.com/?s=" + SearchWord
    req = requests.get(URL)
    ResultSet = []
    soup = BeautifulSoup(req.content, 'html5lib')
    reports = soup.findAll('div', class_='row align-middle no-padding')
    print(len(reports))

    for i in reports:
        ReportURL = i.find('div', class_='small-12 medium-5 columns').find('a')['href']
        ReportTitle = i.find('div', class_='small-12 medium-7 columns').find('div', class_='post-title').text.strip()
        try:
            Rd = i.find('li', class_='post-date').text.strip()
        except AttributeError:
            Rd = ''

        print(ReportURL)
        SummaryRequest = requests.get(ReportURL)
        soup2 = BeautifulSoup(SummaryRequest.content, 'html5lib')
        try:
            ReportSummary = soup2.find('div', class_='post-title-container').find('p').text.strip()
        except AttributeError:
            ReportSummary = soup2.find('div', class_='post-content entry-content').findAll('p')[1].text.strip()

        if (Rd == ''):
            Rd = soup2.find('div', class_='thb-post-date').text.strip()
        print(ReportTitle)
        print(ReportSummary)
        print(Rd)
        date = dateparser.parse(Rd)
        day = date.day
        month = date.month
        year = date.year
        print(day, month, year)
        Vals = (ReportTitle, ReportURL, ReportSummary, day, month, year, 'The Rakyat Post')
        ResultSet.append(Vals)

    return ResultSet


# print(ReportURL)


if __name__ == "__main__":
    SearchWord = 'BIO'
    results = TRP_scrapper(SearchWord)
    print(results)
