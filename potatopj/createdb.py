import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='potato'
)

# prepare a cursor object
cursorObect = dataBase.cursor()

# Create a database
cursorObect.execute("CREATE DATABASE potato")

print("Database created")
