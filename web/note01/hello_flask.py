"""
Refer: https://hackmd.io/@shaoeChen/SyP4YEnef?type=view
"""

from flask import Flask

#Flask 類別 初始化時 傳入的 __name__ 參數，代表當前模組的名稱。是固定用法，以便讓 Flask 知道在哪裡尋找資源。
app = Flask(__name__)

# flask利用裝飾器@app.route來定義路由
@app.route('/')
# 當你連接到’/'的時候，路由就知道要執行後面的function了
def index():
    return 'hello man'

if __name__ == '__main__':
    app.debug = True
    app.run()