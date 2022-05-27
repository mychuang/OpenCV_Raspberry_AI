
import numpy as np
from flask import Flask
from flask import jsonify
from flask_cors import CORS
from flask import render_template, request, redirect, url_for, session

#//Flask 類別 初始化時 傳入的 __name__ 參數，代表當前模組的名稱。是固定用法，以便讓 Flask 知道在哪裡尋找資源。
app = Flask(__name__)

#裝飾器是告訴 Flask，哪個 URL 應該觸發我們的函式。
#斜線代表的就是網站的根目錄，可以疊加。
@app.route("/")
def home():
    return render_template('home.html')

@app.route("/login")
def login_html():
    return render_template("login.html")

@app.route("/baseHome")
def home_html():
    return render_template("baseHome.html")

if __name__ == '__main__':
    app.run()

