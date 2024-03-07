# Frontend
    # html, css, javascript

# Backend
    # Python

# Framework
    # Flask -> pip install flask

# Ambiente virtual -> Local no computador com instalaçoes específicas
    # ctrl + ship + p -> abre barra de comandos
    # environment -> python

# importar o flask
from flask import Flask, render_template

# criar o app
app = Flask(__name__)

# criar a primeira pagina - primeira rota
@app.route("/")
def homepage():
    return render_template("homepage.html")

# roda o aplicativo
app.run()

# websocket