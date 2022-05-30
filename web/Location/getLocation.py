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
    return render_template('index.html')

@app.route('/setRequest', methods=['GET', 'POST'])
def setData():
    location['lat'] = request.form.get('lat')
    location['lon'] = request.form.get('lon')
    location['date'] = request.form.get('date')
    return json.dumps({"msg": "set success"})

if __name__ == '__main__':
    app.debug = True
    app.run()