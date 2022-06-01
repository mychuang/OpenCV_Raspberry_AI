from flask import Flask, url_for, redirect, render_template, request, session
import json
import WeatherData as wd
from datetime import datetime
import pymysql as mysql

sqlFlag = False
try:
    db = mysql.connect(host="localhost", user="mychuang", passwd="vipoo202", db="db")
    cursor = db.cursor()
    print("sucess to connect to sql")
    sqlFlag = True
except:
    print("cannot use sql")

app = Flask(__name__)

@app.route('/')
def login():
    if "user" in session:
        return redirect(url_for("home"))

    return render_template('login.html')

@app.route('/setRequest', methods=['GET', 'POST'])
def setData():
    global sqlFlag

    if(sqlFlag):
        # 確認使用者身分
        sql = "SELECT * FROM users WHERE name=" + "'" + request.form.get('user') + "'"
        cursor.execute(sql)
        user = cursor.fetchone()
        cursor.close()

        if user == None:
            print("Non user in database")
            return render_template('login.html')
        if len(user) > 0:
            session["pwd"] = request.form.get('pwd')
            session["user"] = request.form.get('user')
            session['lat'] = request.form.get('lat')
            session['lon'] = request.form.get('lon')
            session['date'] = request.form.get('date')

            # get weather
            Times = session['date'].split('-', 2)
            try:
                weatherObs = wd.obs.get(lat=float(session['lat']), lon=float(session['lon']),
                                        dtime=datetime(int(Times[0]), int(Times[1]), int(Times[2])))
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
    else:
        session["pwd"] = request.form.get('pwd')
        session["user"] = request.form.get('user')
        session['lat'] = request.form.get('lat')
        session['lon'] = request.form.get('lon')
        session['date'] = request.form.get('date')
        # get weather
        Times = session['date'].split('-', 2)
        try:
            weatherObs = wd.obs.get(lat=float(session['lat']), lon=float(session['lon']),
                        dtime=datetime(int(Times[0]), int(Times[1]), int(Times[2])))
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
    if "user" in session:
        return redirect(url_for("home"))

    return render_template('regist.html')

@app.route("/setRegist", methods=['GET', 'POST'])
def setRegist():
    if (sqlFlag):
        sql = "SELECT COUNT(id) FROM users"
        cursor.execute(sql)
        result = cursor.fetchone()
        cursor.close()
        id = result[0] + 1

        var1 = "'" + str(id) + "',"
        var2 = "'" + request.form.get('user') + "',"
        var3 = "'" + request.form.get('email') + "',"
        var4 = "'" + request.form.get('pwd') + "'"
        sql = "INSERT INTO users VALUES (" + var1 + var2 + var3 + var4 + ");"
        print(sql)
        cursor.execute(sql)
        db.commit()  # send sql

    else:
        print(request.form.get('pwd'))
        print(request.form.get('user'))
        print(request.form.get('email'))

    return json.dumps({"msg": "success"})

if __name__ == '__main__':
    app.debug = True
    app.secret_key = "#230dec61-fee8-4ef2-a791-36f9e680c9fc"
    if (sqlFlag):
        app.run(host="0.0.0.0", port=8888)
    else:
        app.run()