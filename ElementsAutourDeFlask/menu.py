from flask_wtf import Form
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired

class MyForm(Form):
    lang = SelectField(u'Programming Language', 
                choices=[('cpp', 'C++'), ('py', 'Python'), 
                         ('text', 'Plain Text')], 
                      id = 'selectmenu')
    submit = SubmitField('Go')
    
from flask import Flask, flash, redirect, render_template, \
     request, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'


@app.route('/menu', methods=('GET', 'POST'))
def menu():
    form = MyForm()
    if form.validate_on_submit():
        return redirect('/success/'+form.lang.data)
    return render_template('menu.html', form=form)

@app.route('/success/<lang>')
def success(lang):
    return "Le choix effectué est " + lang + ".\n"


if __name__=='__main__':
    app.run(debug=True, port=2747)