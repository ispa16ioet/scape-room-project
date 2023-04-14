import os

from flask import Flask, render_template
import questions
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

@app.route('/questiont/<id>')
def questiont(id):
    data = questions.questions
    print(data[int(id)])
    return render_template('questiont.html',data = data[int(id)])

@app.route('/validate/<id>/<answerd>')
def validate(id,answerd):
    data = questions.questions
    print(data[int(id)])
    return render_template('questiont.html',data = data[int(id)])


if __name__ == '__main__':
    app.run(debug=True)