import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
     database="Example1"
)
cr=db.cursor()
sql = "INSERT INTO user (name, number) VALUES (%s, %s)"
val = [
 ('Peter', '4'),
 ('Amy', ' 652'),]
cr.executemany(sql, val)

db.commit()

print(cr.rowcount, "record inserted.")