from flask import Flask, url_for, redirect, render_template, request, session
import json
import WeatherData as wd
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def login():
    if "user" in session:
        return redirect(url_for("home"))

    return render_template('login.html')

@app.route('/setRequest', methods=['GET', 'POST'])
def setData():
    session["pwd"] = request.form.get('pwd')
    session["user"] = request.form.get('user')
    session['lat'] = request.form.get('lat')
    session['lon'] = request.form.get('lon')
    session['date'] = request.form.get('date')
    print(session['lat'])
    print(session['lon'])
    # get weather
    Times = session['date'].split('-', 2)
    try:
        weatherObs = wd.obs.get(lat=float(session['lat']), lon=float(session['lon']),
                        dtime=datetime(int(Times[0]), int(Times[1]), int(Times[2])))
        print("get temp ", weatherObs['tx'])
        session['ws'] = weatherObs['ws']
        session['tx'] = weatherObs['tx']
        session['pres'] = weatherObs['pres']
        session['precp_hour'] = weatherObs['precp_hour']
    except:
        print("setData: error occures when get obs")
        session['ws'] = -999.9
        session['tx'] = -999.9
        session['pres'] = -999.9
        session['precp_hour'] = -999.9

    return json.dumps({"msg": "success"})

@app.route('/home')
def home():
    global data
    if 'user' in session.keys() and 'lat' in session.keys():
        return render_template('home.html',
                               user_key=session["user"], lat_key=session['lat'], lon_key=session['lon'],
                               ws_key=session['ws'], tx_key=session['tx'], pres_key=session['pres'],
                               precp_key=session['precp_hour'])
    return render_template('login.html')

@app.route("/logout")
def logout():
    session.pop("user", None)
    session.pop("lat", None)
    session.pop("lon", None)
    session.pop("ws", None)
    session.pop("tx", None)
    session.pop("pres", None)
    session.pop("precp_hour", None)
    return redirect(url_for("login"))

@app.route("/regist")
def regist():
    return render_template('regist.html')

if __name__ == '__main__':
    app.debug = True
    app.secret_key = "#230dec61-fee8-4ef2-a791-36f9e680c9fc"
    app.run()