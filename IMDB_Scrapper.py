import mysql.connector
import requests
from datetime import datetime, timezone
from bs4 import BeautifulSoup

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="hbits"
)
mycursor=mydb.cursor()

URL="https://m.imdb.com/chart/top/"
req = requests.get(URL)

soup = BeautifulSoup(req.content, 'html5lib')
# print(soup.prettify())

movie=soup.findAll('div', {'class':'col-xs-12 col-md-6'})
print(len(movie))

# Looping through each movie
for i in range(10,len(movie)):
    # print(movie[i])
    logo=movie[i].find('span', {'class':'pull-left poster-wrap ribbonize'}).find('a').find('img')['src']
    print("Logo: " + logo)

    title=movie[i].find('a', {'class':'btn-full'})
    profile='https://m.imdb.com'+title['href']
    print("Profile URL: " + profile)

    movie_title_name=title.find('h4').text.strip().replace('\n',' ')
    movie_title_name=movie_title_name[movie_title_name.find('. ')+2:]
    print("Movie Name: " + movie_title_name)

    ratings=title.find('p', {'class':'h4 unbold'}).findAll('span')[1].text
    print('Ratings: ' + ratings)

    time = datetime.now()
    print(time)
    print("\n\n\n")
    vals=(movie_title_name,profile,logo,ratings,time)
    sql=("""Insert into sys.imdb_ratings_data(Movie_Name, Profile, Logo, Rating, Timestamp) Values(%s,%s,%s,%s,%s)""")
    mycursor.execute(sql, vals)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

    # try:
    #
    #     mydb.commit()
    # except:
    #     mydb.rollback()
    #     break
print(mydb)