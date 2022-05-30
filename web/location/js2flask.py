from flask import Flask
from flask import url_for
from flask import redirect
from flask import render_template
from flask import request
import json

app = Flask(__name__)
testInfo = {}

@app.route('/')
def loginFunction():
    return render_template('js2flask.html')

@app.route('/getRequest', methods=['GET', 'POST'])
def test():
    testInfo['name'] = 'mychuang'
    testInfo['age'] = '30'
    return json.dumps(testInfo)


if __name__ == '__main__':
    app.debug = True
    app.run()