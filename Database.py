import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)
cr=db.cursor()
cr.execute("CREATE DATABASE Example1")
cr.execute("SHOW DATABASE Example1")
db.close()
