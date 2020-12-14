from flask import Flask, send_file
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def index():
    texte = "ceci est un texte accentué où il y a des trucs".encode('utf8')
    return send_file(BytesIO(texte),
                     attachment_filename="testing.txt",
                     as_attachment=True)
        
app.run(debug=True)