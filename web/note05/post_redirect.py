"""
Refer: https://hackmd.io/@shaoeChen/rkpy9CGZz?type=view
"""

from flask import Flask
from flask import url_for
from flask import redirect
from flask import render_template
from flask import request
from flask import flash
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def loginFunction():
    if request.method == 'POST':
        if login_check(request.form['username']):
            flash('Login Success!')
            return redirect(url_for('hello', username=request.form.get('username')))

    return render_template('login.html')

def login_check(username):
    """登入帳號密碼檢核"""
    if username == 'admin':
        return True
    else:
        return False

@app.route('/hello/<username>')
def hello(username):
    return render_template('user.html', username=username)

if __name__ == '__main__':
    app.debug = True
    app.secret_key = "Your Key"
    app.run()