import random
from flask import render_template, request
from app import app

@app.route('/')
@app.route('/index')
def index():
    advice = [
        "Hygiene is optional",
        "Get yourself a cookie",
        "Try not to talk too much in the morning",
        "Walk softly and be sure to hit goal steps",
        "Don't fart in your sleeping bag",
        "Toenails are for quitters"
    ]

    # if request.method == 'POST':
    #     if 'advice' in request.form:
    #         return render_template('index.html', advice=random.choice(advice))
    # elif request.method == 'GET':
        
    return render_template('index.html', advice=random.choice(advice))


@app.route('/gina')
def gina():
    return render_template('gina.html')
