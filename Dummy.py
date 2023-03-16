import mysql.connector
import pymysql
import pandas as pd
from sqlalchemy import create_engine, text
import datetime

# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="hbits"
# )
# mycursor = mydb.cursor()

mydb_sqlalchemy = create_engine("mysql+pymysql://{user}:{pw}@localhost/sys"
                                .format(user="root", pw="hbits"))
data = pd.DataFrame({"ID": ['1'], 'book_name': ['XYZ'], 'book_author': ['JAMES']})
data=data.set_index('ID',verify_integrity=True)
print(data)
data.to_sql('book_details', con=mydb_sqlalchemy, if_exists='append', chunksize=1000)

# AppName = 'CANKADO PRO-React Onco'
# appID= pd.read_sql(text("""Select ID from sys.tbldigafarm WHERE AppName= :AppName;"""), params={'AppName':AppName}, con=mydb_sqlalchemy.connect())
# print(appID)
# # print(type)
# print(appID['ID'][0])


# mycursor.execute("Select ID from sys.tbldigafarm WHERE AppName='"+AppName+"'")
# AppID=mycursor.fetchall()
# print(AppID[0])
# print(pd.options.display.max_rows)
# URL = "https://apps.apple.com/us/app/beme-teen-mental-health/id1595828671"
# req = requests.get(URL)
# soup = BeautifulSoup(req.content, 'html5lib')

a = datetime.datetime(2017, 6, 21, 18, 25, 30)
b = datetime.datetime(2017, 5, 16, 8, 21, 10)

# returns a timedelta object
c = a - b
print('Difference: ', c)