import os

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/next')
def next():
    return render_template('next.html')

@app.route('/question')
def question():
    return render_template('question.html')

@app.route('/questiont')
def questiont():
    return render_template('questiont.html')


if __name__ == '__main__':
    app.run(debug=True)