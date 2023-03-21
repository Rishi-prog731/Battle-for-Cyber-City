from flask import Flask, render_template
from flask_sock import Sock

app = Flask(__name__)
sock = Sock(app)

@app.get('/')
def default():
    return render_template('default.html.jinja', title='Default')

@sock.route('/<route>')
def ws(ws, route):
    while True:
        message = ws.receive()
        ws.send(message)