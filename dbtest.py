import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="pythonuser",
  passwd="Abcd1234!"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)
