from flask import Flask, render_template

app = Flask(__name__)

@app.get('/')
def default():
    return render_template('default.html.jinja')