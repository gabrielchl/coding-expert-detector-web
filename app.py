from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return 'home page'


@app.route('/result')
def result():
    return 'result page'
