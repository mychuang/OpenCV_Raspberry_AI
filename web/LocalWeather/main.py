from flask import Flask, url_for, redirect, render_template, request, session
import json
import WeatherData as wd
from datetime import datetime

app = Flask(__name__)
data = {}

# flask利用裝飾器@app.route來定義路由
@app.route('/')
# 當你連接到’/'的時候，路由就知道要執行後面的function了
def login():
    return render_template('login.html')

@app.route('/setRequest', methods=['GET', 'POST'])
def setData():
    data['user'] = request.form.get('user')
    data['lat'] = request.form.get('lat')
    data['lon'] = request.form.get('lon')
    data['date'] = request.form.get('date')

    # get weather
    Times = data['date'].split('-', 2)
    weatherObs = wd.obs.get(lat=float(data['lat']), lon=float(data['lon']),
                        dtime=datetime(int(Times[0]), int(Times[1]), int(Times[2])))
    data['ws'] = weatherObs['ws']
    data['tx'] = weatherObs['tx']
    data['pres'] = weatherObs['pres']
    data['precp_hour'] = weatherObs['precp_hour']

    return json.dumps({"msg": "success"})

@app.route('/home')
# 當你連接到’/'的時候，路由就知道要執行後面的function了
def home():
    return render_template('home.html',
                           user_key=data['user'], lat_key=data['lat'], lon_key=data['lon'],
                           ws_key=data['ws'], tx_key=data['tx'], pres_key=data['pres'], precp_key=data['precp_hour'])

if __name__ == '__main__':
    app.debug = True
    app.run()