from flask import Flask, flash, session, request, redirect, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/planes')
def planes():
    return render_template('planes.html')

@app.route('/trains')
def trains():
    return render_template('trains.html')

@app.route('/automobiles')
def automobiles():
    return render_template('automobiles.html')

@app.route('/boats')
def boats():
    return render_template('boats.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

app.run(debug=True)