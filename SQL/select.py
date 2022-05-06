import pymysql as mysql

db = mysql.connect(host="localhost", user="mychuang", passwd="vipoo202", db="mydatabase")

cursor = db.cursor() #connect

sql = "INSERT INTO mytable (value01, value02, value03,value04) VALUES ('A','B','C','D');"
cursor.execute(sql) #ececute the sql statment
db.commit() #send sql

sql = "SELECT * FROM mytable;"
cursor.execute(sql) #ececute the sql statment

result = cursor.fetchall()

for record in result:
    print("value01=%s value02=%s value03=%s value04=%s" %(record[0],record[1],record[2],record[3]))
