import os
from flask import Blueprint, Flask, jsonify, session, redirect, url_for, escape, \
    request, send_from_directory, app
from flask import render_template
from whitenoise import WhiteNoise

app = Flask(__name__)
app.wsgi_app = WhiteNoise(app.wsgi_app, root='static/')

app.secret_key = b'\xe5\xc3\x0c\xee(\x99\x1fxV\x93K4q \xb8\xa4'


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/project_base")
def render_project_base():
    return render_template("projects/project_base.html")

@app.route("/project_pleats_please")
def render_pleats_please():
    return render_template("projects/pleats_please.html")



if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
