from flask import Flask, render_template, url_for, redirect, g, request
import random

app = Flask(__name__)

@app.route('/', methods=["POST","GET"])
def index():
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.form.get('up'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.form.get('spcl'):
        characters.extend(list('!@#$%^&*~()_+?'))

    if request.form.get('num'):
        characters.extend(list('0123456789'))

    length = request.form.get('length', type=int)
    pas = ""
    for x in range(length):
        pas += random.choice(characters)

    return render_template('index.html', pas=pas)

if __name__ == '__main__':
    app.run(debug=True)
