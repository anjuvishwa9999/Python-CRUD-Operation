import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
     database="Example1"
)
cr=db.cursor()
sql = "UPDATE user SET number = ' 123' WHERE name = 'Amy'"

cr.execute(sql)

db.commit()

print(cr.rowcount, "record(s) affected")