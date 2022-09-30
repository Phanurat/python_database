from pickle import TRUE
import pymysql

# database connection
connection = pymysql.connect(
    host="localhost", 
    port=3306, 
    user="root", 
    passwd="", 
    database="list_db")


#Data Check to Connecting!!
if connection != False:
    print("Connecting to Successfully!")

else:
    print("Error to Connecting!!!")

#Is mean Method to syntax from SQL other add, delete, edit, show
cursor = connection.cursor()

#SQL Syntax
sel = "SELECT * FROM test_db"

#Hook Data on Database SQL to use
cursor.execute(sel)

#Cursor Mark to Position
records = cursor.fetchall()
print("List ==> ", cursor.rowcount)

#Loop for Show Data
for row in records:
    print("id ==> ", row[0])
    print("name ==> ", row[1])
    print("last ==> ", row[2])
    print("password ==> ", row[3])

cursor = connection.cursor()
# some other statements  with the help of cursor
connection.close()