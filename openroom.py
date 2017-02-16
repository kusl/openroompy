from flask import Flask

from Animal import Dog

app = Flask(__name__)


@app.route('/')
def hello_world():
    fido = Dog.Dog('Fido')
    fido.add_trick('roll over')
    fido.add_trick('play dead')
    return str(len(fido.tricks))


if __name__ == '__main__':
    app.run(debug=True)
