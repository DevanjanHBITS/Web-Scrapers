from typing import Any
import dateparser
import mysql.connector
import requests

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="hbits"
)
mycursor = mydb.cursor()

# soup=BeautifulSoup(req.content, 'html5lib')
    # print(soup.prettify())
    # print(req)
    # data=json.loads(req)
    # print(json.dumps(req, indent=1))

# head={
# ":authority": "api.news.ontario.ca"
# ":method": 'GET'
# ':path': "/api/v1/releases?language=en&sort=desc&limit=10&page=1"
# ":scheme": 'https'
# "accept": "application/json, text/plain, */*"
# "accept-encoding": 'gzip, deflate, br'
# 'accept-language': 'en-US,en;q=0.9'
# 'origin': 'https://news.ontario.ca'
# 'referer': 'https://news.ontario.ca/'
# 'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"'
# 'sec-ch-ua-mobile': '?0'
# 'sec-ch-ua-platform': "\"Windows\""
# 'sec-fetch-dest': 'empty'
# 'sec-fetch-mode': 'cors'
# 'sec-fetch-site': 'same-site'
# 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
# }

def Ontario(SearchWord):
    URL = "https://api.news.ontario.ca/api/v1/search?language=en&keywords=" + SearchWord + "&sort=desc&limit=10&page=1"
    req = requests.get(URL).json()
    print(type(req['data']))
    News = req['data']
    print(len(News))
    NewsList=[]

    for i in News:
        NewsTitle = i['content_title']
        print(NewsTitle)
        NewsSummary = i['content_lead'].replace('<p>', '').replace('</p>', '').replace('&mdash;', '—').replace(
            '&rsquo;', "'").replace('<strong>', '').replace('</strong>', '')
        print(NewsSummary)
        NewsDate = i['release_date_time_formatted']
        NewsDate = dateparser.parse(NewsDate)
        day = NewsDate.day
        month = NewsDate.month
        year = NewsDate.year
        print(day, month, year)
        vals: tuple[Any, Any, int, int, int, str]=(NewsTitle, NewsSummary, day, month, year, 'Ontario')
        print(vals)
        NewsList.append(vals)
    return NewsList

if __name__ == '__main__':
    # URL = "https://api.news.ontario.ca/api/v1/releases?language=en&sort=desc&limit=10&page=1"
    SearchWord='Bio'
    # URL2="https://api.news.ontario.ca/api/v1/search?language=en&keywords="+SearchWord+"&sort=desc&limit=10&page=1"
    x=Ontario(SearchWord)
    print(len(x))
    print(x)
