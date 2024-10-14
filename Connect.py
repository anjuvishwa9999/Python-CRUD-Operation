import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="_Passw#999"
)
print(db)

if db.is_connected():
    print("conection")
else:
    print("fail")