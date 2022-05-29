import pymysql as mysql

db = mysql.connect(host="localhost", user="mychuang", passwd="vipoo202", db="db")

cursor = db.cursor() #connect
cursor.execute("SELECT * FROM users WHERE name='Miller'")

user = cursor.fetchone()
cursor.close()

print(user)
print(len(user))
print(user[0])
print(user[1])
print(user[2])
print(user[3])
