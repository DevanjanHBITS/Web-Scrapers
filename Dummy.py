import mysql.connector
import numpy.random
import pymysql
import pandas as pd
from collections import namedtuple
from dataclasses import make_dataclass
from sqlalchemy import create_engine, text
import datetime
import numpy as np

# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="hbits"
# )
# mycursor = mydb.cursor()

# SQL Alchemy
# mydb_sqlalchemy = create_engine("mysql+pymysql://{user}:{pw}@localhost/sys"
#                                 .format(user="root", pw="hbits"))
# data = pd.DataFrame({"ID": ['1'], 'book_name': ['XYZ'], 'book_author': ['JAMES']})
# data=data.set_index('ID',verify_integrity=True)
# print(data)
# data.to_sql('book_details', con=mydb_sqlalchemy, if_exists='append', chunksize=1000)

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


# DateTime Parsers
# a = datetime.datetime(2017, 6, 21, 18, 25, 30)
# b = datetime.datetime(2017, 5, 16, 8, 21, 10)
#
# # returns a timedelta object
# c = a - b
# print('Difference: ', c)


# Pandas Series
# list=list(range(1,101))
# x= numpy.random.randint(low=10,high=1000, size=100)
# # print(type(x))
# # print(x)
# # list=list(range(1,151))
# # print(list)
# s=pd.Series(x, index=list)
# # print(s)
#
# d = {"A": 0.0, "b": 1.0, "c": 2.0, "e": 3.0}
# print(pd.Series(d, index=["b", "c", "d", "a", "e"]))
# print(pd.Series(5.0, index=["a", "b", "c", "d", "e"]))
# print(s[1:50:2])
# # print(s.index)
# # print(s.to_numpy())
# print(s[12])
# s.get([101], np.nan)
# print(s[101])

d = {
    "one": pd.Series([1.0, 2.0, 3.0], index=["a", "b", "c"]),
    "two": pd.Series([1.0, 2.0, 3.0, 4.0], index=["a", "b", "c", "d"]),
}

df = pd.DataFrame(d, index=["d", "b", "a", "c", "e"], columns=["one", "two", "three"])
print(df)
print(df.index)

data = [{"a": 1, "b": 2, "c": 70.0}, {"a": 5, "b": 10, "c": 20}]
df = pd.DataFrame(data, index=['1', '2'])
print(df)

Point = namedtuple("Point", "x y")
# Point = make_dataclass("Point", [("x", int), ("y", int)])
df = pd.DataFrame([Point(0, 0), Point(1, 1), (2, 2)])
print(df)

iris_df = pd.read_csv("Iris.csv")
iris_df.set_index("Id", verify_integrity=True)
print(iris_df)
# print(iris_df.index)
iris_df1 = iris_df.assign(sepal_ratio=lambda x: (x["SepalWidthCm"] / x["SepalLengthCm"])).head(70)
iris_df1.set_index("Id", verify_integrity=True)
iris_df1=iris_df1+iris_df
print(iris_df1.to_string())
# print(iris_df1.index)