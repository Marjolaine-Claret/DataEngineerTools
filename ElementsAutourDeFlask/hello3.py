from flask import Flask
app = Flask(__name__)  

from flask import request

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print(request.form)
        username = request.form.get('username')
        password = request.form.get('password')
        return 'Hello ' + username
        #do_the_login()
    else:
        #pass #show_the_login_form()
        print('pas POST')
        username = request.args.get('username') # décode l'URL et reconnaît chacun des champs
        password = request.args.get('password')
        return 'Hello ' + username
    return 'Nobody connected'

if __name__ == '__main__':
    app.run(debug=True, port=2745)     
