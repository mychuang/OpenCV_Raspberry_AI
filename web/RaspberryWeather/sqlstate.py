import pymysql as mysql

db = mysql.connect(host="localhost", user="mychuang", passwd="vipoo202", db="db")
cursor = db.cursor()

sql = "SELECT COUNT(id) FROM users"
cursor.execute(sql)
result = cursor.fetchone()
cursor.close()
id = result[0] + 1

var1 = "'" + str(id) + "',"
sql = "INSERT INTO users VALUES (" + var1 + " 'Miller.Huang','hhjoy222@yahoo.com.tw','Vipoo202');"
print(sql)
cursor.execute(sql)
db.commit()  # send sql