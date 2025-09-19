from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/navn')
def navn():
    return 'Navn: Johan'

@app.route('/alder')
def alder():
    return 'Alder: 25'

@app.route('/bosted')
def bosted():
    return 'Bosted: Oslo'

@app.route('/jobb')
def jobb():
    return 'Jobb: Programmer'

if __name__ == '__main__':
    app.run()