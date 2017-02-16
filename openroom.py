from flask import Flask

from Animal import Dog

app = Flask(__name__)


@app.route('/')
def hello_world():
    fido = Dog.Dog('Fido')
    return fido.name


if __name__ == '__main__':
    app.run(debug=True)
