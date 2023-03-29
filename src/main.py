from flask import Flask, render_template
from flask_sock import Sock

from python.modbus import Modbus
modbus = Modbus()
modbus.connect()

modbus.disconnect()

app = Flask(__name__)
sock = Sock(app)

@app.get('/')
def default():
    return render_template('default.jinja', title='Default')

@sock.route('/<route>')
def ws(ws, route):
    while True:
        message = ws.receive()
        print(message)
        ws.send(route)