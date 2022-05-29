import pymysql
from flask import Flask
from flask import url_for
from flask import redirect
from flask import render_template
from flask import request

# 連線資料庫
db = pymysql.connect(host="localhost", user="mychuang", passwd="vipoo202", db="db")  # 連線資料庫
cursor = db.cursor()  # 定義遊標

#Flask 類別 初始化時 傳入的 __name__ 參數，代表當前模組的名稱。是固定用法，以便讓 Flask 知道在哪裡尋找資源。
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/login", methods=["GET", "POST"])
def login_html():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password'].encode('utf-8')
        cursor.execute("SELECT * FROM users WHERE name='%s'", name)
        user = cursor.fetchone()
        cursor.close()

        if user == None:
            return "沒有這個帳號"
        if len(user) != 0:
            return "login success"
    else:
        return render_template("login.html")

@app.route("/baseHome")
def home_html():
    return render_template("baseHome.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7777)

