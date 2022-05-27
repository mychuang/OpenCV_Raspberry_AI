
import numpy as np
from flask import Flask
from flask import jsonify
from flask_cors import CORS
from flask import render_template, request, redirect, url_for, session

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template("home.html")

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)


