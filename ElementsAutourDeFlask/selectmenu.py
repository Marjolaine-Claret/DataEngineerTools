#!/usr/bin/env python
from flask import Flask, flash, redirect, render_template, \
     request, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template(
        'select_menu.html',
        data=[{'name':'red'}, {'name':'green'}, {'name':'blue'}])

@app.route("/test" , methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        select = request.form.get('comp_select')
        return '<font color="{0}"> {0} </font>'.format(str(select))
    return redirect(url_for('index'))
    

if __name__=='__main__':
    app.run(debug=True, port=2745)