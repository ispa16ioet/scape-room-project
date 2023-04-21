import os

from flask import Flask, render_template,jsonify
import questions
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/next')
def next():
    return render_template('next.html')

@app.route('/intro')
def question():
    return render_template('intro.html')


@app.route('/endgame')
def endgame():
    return render_template('endGame.html')


@app.route('/questiont/<id>')
def questiont(id):
    data = questions.questions
    print(data[int(id)])
    return render_template('questiont.html',data = data[int(id)])

@app.route('/validate/<id>/<answer>')
def validate(id,answer):
    print(id,answer)
    anws= {'anws':'false'}
    data = questions.questions
    if answer == str(data[int(id)]['answer']):
        anwse= {'anws':'true',
               'photo':data[int(id)]['photo'],
               'next':data[int(id)]['next'],
               'nextUbi':data[int(id)]['nextUbi'],
               }
        return jsonify(anwse)
    return jsonify(anws)
if __name__ == '__main__':
    app.run(debug=True)