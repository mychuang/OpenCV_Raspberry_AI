"""
Refer: https://hackmd.io/@shaoeChen/H1CMTVheG?type=view
"""

from flask import Flask
from flask import url_for
from flask import redirect
app = Flask(__name__)

# flask利用裝飾器@app.route來定義路由
@app.route('/')
# 當你連接到’/'的時候，路由就知道要執行後面的function了
def index():
    return 'hello man'

@app.route('/a')
def url_for_a():
    return 'here is a'

@app.route('/b')
def b():
    # url_for_a當做url_for的參數
    # redirect 會將使用者引導到'/a'這個路由
    return redirect(url_for('url_for_a'))

# flask的route設置是可以允許傳遞參數，透過參數的設置我們可以做分頁、搜尋某筆資料時傳遞pk值…等。
@app.route('/user/<username>')
def username(username):
    return 'i am ' + username
# ex: url =  http://127.0.0.1:5000/user/miller

if __name__ == '__main__':
    app.debug = True
    app.run()