import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)
print(db)

if db.is_connected():
    print("conection")
else:
    print("fail")