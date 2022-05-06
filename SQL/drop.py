import pymysql as mysql

db = mysql.connect(host="localhost", user="mychuang", passwd="vipoo202", db="mydatabase")

cursor = db.cursor() #connect

sql = "DROP DATABASE testDataBase;"
cursor.execute(sql) #ececute the sql statment
db.commit() #send sql


sql = "DROP TABLE test;"
cursor.execute(sql) #ececute the sql statment
db.commit() #send sql
