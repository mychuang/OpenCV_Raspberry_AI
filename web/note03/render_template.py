"""
Refer: https://hackmd.io/@shaoeChen/HJkOuSagf?type=view

flask預設模板語法是jinja2
直觀來看，當return render_template('html文件')的時候，
flask會先到專案資料夾『templates』去尋找相對應的html文件
"""

from flask import Flask
from flask import url_for
from flask import redirect
from flask import render_template

app = Flask(__name__)

# flask利用裝飾器@app.route來定義路由
@app.route('/')
# 當你連接到’/'的時候，路由就知道要執行後面的function了
def index():
    return render_template('home.html')

# flask的route設置是可以允許傳遞參數，透過參數的設置我們可以做分頁、搜尋某筆資料時傳遞pk值…等。
@app.route('/user/<username>')
def username(username):
    # user_template是送到jinja2的參數，username是內容，這內容來自於路由參數
    # html需要做對應調整，要設置接收由後端所傳過來的參數user_template: check user.html
    return render_template('user.html', user_template=username)
# ex: url =  http://127.0.0.1:5000/user/miller

if __name__ == '__main__':
    app.debug = True
    app.run()