from flask import Flask
app = Flask(__name__) # crée une application

@app.route('/') # enrobage : route appelle app lorsque l'on est à la racine car / (si on avait eu /b on aurait mis le port + /b pour l'exécuter)
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True, port=2745) 
