import mysql.connector
cnx= mysql.connector.connect(host="localhost", user="root", passwd="naveedali@123")
mycursor= cnx.cursor()

#mycursor.execute("CREATE DATABASE Mood")
mycursor.execute("CREATE DATABASE momin5a123")

'''#mycursor.execute("CREATE TABLE EAT(Mood VARCHAR(50) NOT NULL,Meal VARCHAR(50) NOT NULL)")
sqlform="Insert into EAT(Mood,Meal) values(%s,%s)"
EAT=[("Happy", "Pasta"),("Angry","Rice"),("Sad","Pizza")("neutral","Salad")]

mycursor.executemany(sqlform,EAT)

cnx.commit()'''
'''

mycursor.execute("Select * from EAT")
myresult=mycursor.fetchall()
for row in myresult:
    print(row)
'''

mycursor.execute("Show databases")

for db in mycursor:
    print(db)
