import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
     database="Example1"
)
cr=db.cursor()
cr.execute("SELECT * FROM user")

myresult = cr.fetchall()

for x in myresult:
  print(x)