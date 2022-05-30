"""
Refer: https://medium.com/seaniap/python-web-flask-%E5%A6%82%E4%BD%95%E9%80%8F%E9%81%8Eform%E5%8F%96%E5%BE%97%E8%B3%87%E6%96%99-7a63ebf9ff1f
"""

from flask import Flask
from flask import url_for
from flask import redirect
from flask import render_template
from flask import request

"""
session可以紀錄我們登入（login）的帳號資訊，
讓我們在之後瀏覽這個網站的其他頁面可以繼續使用這個session資訊作為判斷。
如此，我們不用每次進入一個頁面，就要重新再登入一次。
當你離開這個網站，或者是登出（logout）這個網站服務時，session儲存的資訊也會跟著消失無蹤。
"""
from flask import session

app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]

        # session的型態是字典，我們可以指定一個名稱（user）為字典的key，
        # 並且將form表單而來的user值賦予它（user = request.form[“nm”] ）
        session["user"] = user

        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))

        return render_template("login.html")

@app.route("/user")
# 在user函式中取得傳來的session資料：
def user():
    # 判斷是否從session中取得user這個key
    if "user" in session:
        user = session["user"]
        return render_template('user.html', user_template=user)
    else:
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == '__main__':
    app.debug = True
    app.secret_key = "#230dec61-fee8-4ef2-a791-36f9e680c9fc"
    app.run()