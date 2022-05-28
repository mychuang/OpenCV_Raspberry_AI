import numpy as np
from flask import Flask
from flask import jsonify
from flask_cors import CORS
from flask import render_template, request, redirect, url_for, session, flash

#Flask 類別 初始化時 傳入的 __name__ 參數，代表當前模組的名稱。是固定用法，以便讓 Flask 知道在哪裡尋找資源。
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def testLogin():
    # 利用request取得使用者端傳來的方法為何
    if request.method == 'POST':
        #  利用request取得表單欄位值
        #return 'Hello ' + request.values['username']

        if login_check(request.form['username']):
            flash('Login Success!')

            #redirect(url_for('function'))重新導向，將使用者導到@app.route('/hello/<username>')，並且傳遞參數username
            return redirect(url_for('hello', username=request.form.get('username')))

    #  非POST的時候就會回傳一個空白的模板
    return render_template('testLogin.html')


def login_check(username):
    """登入帳號密碼檢核"""
    if username == 'admin':
        return True
    else:
        return False


@app.route('/hello/<username>')
def hello(username):
    return render_template('helloTestLogin.html', username=username)

if __name__ == '__main__':
    app.secret_key = "Your Key"
    app.run()