"""
Refer: https://hackmd.io/@shaoeChen/SytJ0WTxG?type=view

在flask定義app.route('你的路由')的時候，有幾個參數可以設置
其中methods是用來定義這個路由是否執行相關的GET、POST
取得資訊的時候GET
送出資訊的時候POST
"""

from flask import Flask
from flask import url_for
from flask import redirect
from flask import render_template
from flask import request
app = Flask(__name__)

#設計一個login的頁面來接收使用者的登入帳號密碼，接著回傳一個歡迎的訊息給使用者。
@app.route('/', methods=['GET', 'POST'])
def loginFunction():
    #利用request來補捉使用者端的動作是否為POST，如果是POST就代表是使用者端透過submit所提交過來的資料。
    if request.method == 'POST':
        # 透過request.values['username']，我們可以取得從form過來的username欄位資料
        return 'Hello ' + request.values['username']
    # 非POST的時候就會回傳一個空白的模板
    return render_template('login.html')

if __name__ == '__main__':
    app.debug = True
    app.run()