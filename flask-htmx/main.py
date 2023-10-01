# -*- coding: utf-8 -*-

from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def root():
    return render_template("index.html")


@app.route("/clicked")
def clicked():
    now = datetime.now()
    return render_template("clicked.html", timestamp=now)
