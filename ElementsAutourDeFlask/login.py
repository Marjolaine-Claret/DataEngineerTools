#!/usr/bin/env python
from flask import Flask, flash, redirect, render_template, \
     request, url_for
from flask_login import LoginManager, logout_user, login_required, \
       login_user, current_user, UserMixin
from ldap3 import Connection, ALL, Server

from forms import LoginForm    
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

Bootstrap(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Veuillez vous connecter pour accéder à cette page.'

##
def connect(accountName,password):
    server = Server('dc1.lan.esiee.fr', use_ssl=True, get_info=ALL)
    conn = Connection(server, user="cn=LDAP,ou=comptes_services,ou=utilisateurs,DC=lan,DC=esiee,DC=fr",password="UE=cv,VR1^%Mbj43")
    conn.bind()
    conn.search('DC=lan, DC=esiee, DC=fr', "(&(objectclass=person)(sAMAccountName="+accountName+"))",attributes=['distinguishedName', 'sn', 'telephoneNumber', 'displayName', 'roomNumber', 'givenName','Name'])
    if len(conn.entries)>0:
        DN = conn.entries[0].distinguishedName.value
        conn = Connection(server, user=DN, password=password) 
        if(conn.bind()) :
            return True
    return False
##

class User(UserMixin):
    def __init__(self, id, username=''):
        self.username = username
        self.id = id

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)


@app.route('/')
def rien():
    return "Rien ici... <a href='/login'> voir là </a> "

@app.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if connect(form.login.data, form.password.data):
            u = User(42, form.login.data)
            login_user(u, remember=form.remember_me.data)
            return redirect('/success/'+form.login.data)
    return render_template('login.html', form=form)

@login_required
@app.route('/success/<username>')
def sucess(username):
    return "Salut " + username + ".\nTu es arrivé jusque là. "


@login_required
@app.route('/logout')
def logout():
    logout_user()
    return "you are logged out"


if __name__=='__main__':
    app.run(debug=True, port=2747)