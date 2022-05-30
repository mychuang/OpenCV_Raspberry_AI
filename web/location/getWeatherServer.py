import WeatherData as wd
from datetime import datetime

from flask import Flask
from flask import url_for
from flask import redirect
from flask import render_template
from flask import request

#Flask 類別 初始化時 傳入的 __name__ 參數，代表當前模組的名稱。是固定用法，以便讓 Flask 知道在哪裡尋找資源。
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def connectJS():
    if request.method == 'POST':
        result = request.form['javascript_data']
        return result

    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()