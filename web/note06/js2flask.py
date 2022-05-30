from flask import Flask
from flask import url_for
from flask import redirect
from flask import render_template
from flask import request
import json

app = Flask(__name__)
location = {}

@app.route('/')
def home():
    return render_template('js2flask.html')

@app.route('/getRequest', methods=['GET', 'POST'])
def getData():
    if(len(location) == 0):
        return json.dumps({"msg": "no data"})
    else:
        return json.dumps(location)

@app.route('/setRequest', methods=['GET', 'POST'])
def setData():
    location['lat'] = request.form.get('lat')
    location['lon'] = request.form.get('lon')
    return json.dumps({"msg": "set sucess"})

if __name__ == '__main__':
    app.debug = True
    app.run()