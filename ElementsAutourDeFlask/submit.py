#!/usr/bin/env python
from flask import Flask, flash, redirect, render_template, \
     request, url_for

from forms import MyForm    
    
app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

@app.route('/')
def rien():
    return "Rien ici... <a href='/submit'> voir là </a> "

@app.route('/submit', methods=('GET', 'POST'))
def submit():
    form = MyForm()
    if form.validate_on_submit():
        return redirect('/success/'+form.name.data)
    return render_template('submit.html', form=form)

@app.route('/success/<username>')
def sucess(username):
    return "Salut " + username + ".\nTu es arrivé jusque là. "


if __name__=='__main__':
    app.run(debug=True, port=2747)