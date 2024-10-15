import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Example1"
)
cr=db.cursor()
cr.execute("CREATE TABLE user (name varchar(255),number int(255))")
