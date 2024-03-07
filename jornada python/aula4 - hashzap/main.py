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
from flask_socketio import SocketIO, send


# criar o app
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origin="*")


# funcionalidade de enviar mensagem
@socketio.on("message")
def gerenciar_mensagem(mensagem):
    send(mensagem, broadcast=True)


# criar a primeira pagina - primeira rota
@app.route("/")
def homepage():
    return render_template("index.html")


# roda o aplicativo
socketio.run(app, host="192.168.100.153")

# websocket -> faz a conexão entre duas pessoas que estão usando o mesmo site
# pip install python-socketio flask-socketio simple-websocket