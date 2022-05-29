"""
Refer: https://hackmd.io/@shaoeChen/SyP4YEnef?type=view
"""

from flask import Flask
app = Flask(__name__)

# flask利用裝飾器@app.route來定義路由
@app.route('/')
# 當你連接到’/'的時候，路由就知道要執行後面的function了
def index():
    return 'hello man'

if __name__ == '__main__':
    app.debug = True
    app.run()