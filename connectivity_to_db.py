import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",password="1234",database="hospital")
mycursor=mydb.cursor()
mycursor.execute("select * from patient_details")
for i in mycursor:
    print(i)