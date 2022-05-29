import pymysql as mysql

db = mysql.connect(host="localhost", user="mychuang", passwd="vipoo202", db="mydatabase")

cursor = db.cursor() #connect
cursor.execute("SELECT * FROM users WHERE email=hhjoy222@gmail.com")

user = cursor.fetchone()
cursor.close()

print(user)
