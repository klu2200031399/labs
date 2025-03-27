import mysql.connector

mydb = mysql.connector.connect(
    host = "dbinstance.c5ae4cicab2i.us-east-2.rds.amazonaws.com",
    user = "root",
    password = "Klef1234"
)

if(mydb):
    print("Connected Successfully")
else:
    print("Fail to Connect")