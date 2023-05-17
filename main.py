import os

from flask import Flask, render_template,jsonify
import questions
from flask import Markup

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
    data[int(id)]['text'] = (data[int(id)]['text']).replace('\n', '<br>')
    if id =='16':
        return render_template('questiont2.html',data = data[int(id)])
    if id =='11':
        return render_template('questiont3.html',data = data[int(id)])
    return render_template('questiont.html',data = data[int(id)])

@app.route('/validate/<id>/<answer>')
def validate(id,answer):
    print(id,answer)
    anws= {'anws':'false'}
    data = questions.questions
    rta = answer.lower().replace(',',' ').split( )
    rta2 = str(data[int(id)]['answer']).lower()

    if id == '1':
        print(answer)
        if 'equilatero' in rta:
            print('equilatero')
            
        if 'escaleno' in rta:
            print('escaleno')
        if 'equilatero' in rta:
            print('isosceles')
          
        if 'equilatero' in rta and 'isosceles' in rta and 'escaleno' in rta:
            anwse= {'anws':'true',
               'photo':data[int(id)]['photo'],
               'next':data[int(id)]['next'],
               'nextUbi':data[int(id)]['nextUbi'],
               }
            return jsonify(anwse)
        if 'equilátero' in rta  and 'isósceles' in rta and 'escaleno' in rta:
            anwse= {'anws':'true',
               'photo':data[int(id)]['photo'],
               'next':data[int(id)]['next'],
               'nextUbi':data[int(id)]['nextUbi'],
               }
            return jsonify(anwse)
    if id == '2':
        if 'isosceles' in rta or 'isósceles' in rta:
            anwse= {'anws':'true',
               'photo':data[int(id)]['photo'],
               'next':data[int(id)]['next'],
               'nextUbi':data[int(id)]['nextUbi'],
               }
            return jsonify(anwse)
    if id == '14':
        if 'rectángulo' in rta or 'rectangulo' in rta:
            anwse= {'anws':'true',
               'photo':data[int(id)]['photo'],
               'next':data[int(id)]['next'],
               'nextUbi':data[int(id)]['nextUbi'],
               }
            return jsonify(anwse)
    if id == '15':
        if 'círculo' in rta or 'circulo' in rta:
            anwse= {'anws':'true',
               'photo':data[int(id)]['photo'],
               'next':data[int(id)]['next'],
               'nextUbi':data[int(id)]['nextUbi'],
               }
            return jsonify(anwse)
    if id == '16':
        if 'semejanza' in rta or 'semejansa' in rta:
            anwse= {'anws':'true',
               'photo':data[int(id)]['photo'],
               'next':data[int(id)]['next'],
               'nextUbi':data[int(id)]['nextUbi'],
               }
            return jsonify(anwse)
    print(answer.lower(),rta2.lower())        
    if answer.lower() == rta2.lower():
        

        anwse= {'anws':'true',
               'photo':data[int(id)]['photo'],
               'next':data[int(id)]['next'],
               'nextUbi':data[int(id)]['nextUbi'],
               }
        return jsonify(anwse)
    return jsonify(anws)

if __name__ == '__main__':
    app.run()