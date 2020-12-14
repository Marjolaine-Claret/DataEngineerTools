from flask import Flask, flash, redirect, render_template, \
     request, url_for
from flask_login import LoginManager, logout_user, login_required, \
       login_user, current_user, UserMixin
from ldap3 import Connection, ALL, Server

from forms import LoginForm    
from flask_bootstrap import Bootstrap

UPLOAD_FOLDER = '/tmp/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 # 16 Mb

Bootstrap(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Veuillez vous connecter pour accéder à cette page.'


if __name__=='__main__':
    app.run(debug=True, port=2747)