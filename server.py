from flask import Flask, render_template, request, redirect, session
from random import randint

app = Flask(__name__)
app.secret_key = '123456'

@app.route('/')
def start():
    if 'num' not in session:
        session['num'] =  randint(1, 100)
    if 'try' not in session:
        session['try'] = 0
    return render_template('game.html')

@app.route('/guess', methods = ['POST'])
def check_number():
    session['guess'] = int(request.form['guess_number'])
    session['try'] += 1
    print(session)
    return redirect('/')

@app.route('/reset', methods = ['POST'])
def reset():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug = True)