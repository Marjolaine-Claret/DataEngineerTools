from flask import Flask
app = Flask(__name__)  

from flask import request
from flask import render_template, render_template_string

htmltemplate = """<!doctype html>
<title>Hello</title>
{% if name %}
  <h1>Hello {{ name }}!</h1>
{% else %}
  <h1>Hello, World!</h1>
{% endif %}"""


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template_string(htmltemplate, name=name)
    # return render_template('hello.html', name=name) <-- Permet d'utiliser un fichier de template

if __name__ == '__main__':
    app.run(debug=True, port=2745) 
