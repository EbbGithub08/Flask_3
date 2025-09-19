from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <h1>Her er litt info om meg</h1>
    <ul>
        <li><a href="/navn">Navn</a></li>
        <li><a href="/alder">Alder</a></li>
        <li><a href="/bosted">Bosted</a></li>
        <li><a href="/jobb">Jobb</a></li>
    </ul>
    '''
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