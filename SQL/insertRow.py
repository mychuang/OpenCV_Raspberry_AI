import pymysql as mysql

db = mysql.connect(host="localhost", user="mychuang", passwd="vipoo202", db="mydatabase")

cursor = db.cursor() #connect

sql = "INSERT INTO mytable (value01, value02, value03,value04) VALUES ('10','10','10','10');"

cursor.execute(sql) #ececute the sql statment
db.commit() #send sql
