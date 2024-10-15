import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
     database="Example1"
)
cr=db.cursor()
sql = "DELETE FROM user WHERE number = '4'"

cr.execute(sql)

db.commit()

print(cr.rowcount, "record(s) deleted")