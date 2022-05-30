from flask import Flask
from flask import url_for
from flask import redirect
from flask import render_template
from flask import request
from flask import session
import json

app = Flask(__name__)
location = {}

@app.route("/", methods=["POST","GET"])
def login():
    if request.method == "POST":
        location['user'] = request.form.get('user')
        location['lat'] = request.form.get('lat')
        location['lon'] = request.form.get('lon')
        location['date'] = request.form.get('date')

        session["user"] = location['user']
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))

        return render_template("login.html")

@app.route("/home")
def user():
    # 判斷是否從session中取得user這個key
    if "user" in session:
        user = session["user"]
        return render_template('home.html', user_template=user)
    else:
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == '__main__':
    app.debug = True
    app.secret_key = "#230dec61-fee8-4ef2-a791-36f9e680c9fc"
    app.run()