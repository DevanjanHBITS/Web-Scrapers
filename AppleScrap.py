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


def AppleScrap(URL):
    req = requests.get(URL)
    soup = BeautifulSoup(req.content, 'html5lib')

    AppName = soup.find('h1', class_='product-header__title app-header__title').text.replace('12+', '').rstrip().strip()
    print(AppName)
    AppLogo = \
    soup.find('div', class_='product-hero__media l-column small-5 medium-4 large-3 small-valign-top').find('source')[
        'srcset']
    print(AppLogo)
    AppDeveloper = soup.find('dd',
                             class_='information-list__item__definition information-list__item__definition--copyright').text.replace(
        '© ', '').rstrip().strip()
    print(AppDeveloper)
    AppGenre = soup.findAll('div', class_='information-list__item l-column small-12 medium-6 large-4 small-valign-top')[
        2].find('a').text.rstrip().strip()
    print(AppGenre)
    AppLanguage = \
    soup.findAll('div', class_='information-list__item l-column small-12 medium-6 large-4 small-valign-top')[4].find(
        'p').text.rstrip().strip()
    print(AppLanguage)
    AppRatings = soup.find('div', class_='we-customer-ratings__stats l-column small-4 medium-6 large-4').text.replace(
        '\n        ', ', ').rstrip().strip()
    print(AppRatings)
    AppRatings = AppRatings.split(', ')
    Ratings = AppRatings[0]
    Votes = AppRatings[1]
    print(Ratings)
    print(Votes)
    AppDescription = soup.find('div', class_='section__description').text.replace('\n', '').replace(
        'Description                                ', '').rstrip().strip()
    print(AppDescription)
    AppCompatibility = \
    soup.findAll('div', class_='information-list__item l-column small-12 medium-6 large-4 small-valign-top')[3].find(
        'dd').findAll('dl')
    print(len(AppCompatibility))
    Compatibility = []
    for i in AppCompatibility:
        AppC = i.find('dt').text.rstrip().strip()
        print(AppC)
        Compatibility.append(AppC)

    AppVersion = soup.find('div', class_='l-column small-12 medium-3 large-4 small-valign-top whats-new__latest').find(
        'p').text.rstrip().strip()
    print(AppVersion)

    # print(AppVersions)
    vals = (
    AppName, AppLogo, AppDeveloper, AppGenre, AppLanguage, AppVersion, Ratings, Votes, AppDescription, Compatibility,
    'AppleScrap')
    return vals


if __name__ == "__main__":
    URL = "https://apps.apple.com/us/app/beme-teen-mental-health/id1595828671"
    x = AppleScrap(URL)
    print(x)
