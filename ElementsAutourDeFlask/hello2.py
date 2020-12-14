from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/hello/<username>')
def hello_user(username):
    return 'Hello {}!'.format(username)

@app.route('/hello/<int:user_id>') # s'il reconnaît un entier lance cette page
def hello_userid(user_id):
    return 'Hello user n°{}!'.format(user_id)

@app.errorhandler(404)
def page_not_found(e):
    return 'Nothing to see here'

if __name__ == '__main__':
    app.run(debug=True, port=2745) 
