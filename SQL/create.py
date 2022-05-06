import pymysql as mysql

db = mysql.connect(host="localhost", user="mychuang", passwd="vipoo202", db="mydatabase")

cursor = db.cursor() #connect

sql = "CREATE DATABASE testDataBase;"
cursor.execute(sql) #ececute the sql statment
db.commit() #send sql


sql = "CREATE TABLE test(col01 VARCHAR(255), col02 VARCHAR(255), col03 VARCHAR(255), col04 VARCHAR(255));"
cursor.execute(sql) #ececute the sql statment
db.commit() #send sql
