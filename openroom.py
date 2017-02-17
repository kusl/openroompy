from flask import Flask, request, jsonify

from User import User

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "hello, world"


@app.route('/api/v0/users', methods=['POST'])
def create_user():
    email = request.json['email']
    password = request.json['password']
    user = User
    user.create(user, email=email, password=password)
    return jsonify(user.serialize(user)), 201


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
