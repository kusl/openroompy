from flask import Flask

from Animal import Corgi

app = Flask(__name__)


@app.route('/')
def hello_world():
    fido = Corgi.Corgi('fido')
    fido.add_trick('speak')
    return fido.tricks[0]


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
