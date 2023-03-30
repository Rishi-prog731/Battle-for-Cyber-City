from flask import Flask, render_template
from flask_sock import Sock

app = Flask(__name__)
sock = Sock(app)

@app.get('/hacker')
def hacker():
    return render_template('start.jinja', title='Hacker')

@app.get('/defender')
def defender():
    return render_template('start.jinja', title='Defender')


@sock.route('/<route>')
def ws(ws, route):
    while True:
        message = ws.receive()
        print(message)
        ws.send(route)