from flask import Flask, request, jsonify, url_for

from User import User

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "hello, world"


@app.route('/api/v0/users', methods=['POST'])
def create_user():
    email = request.json['email']
    password = request.json['password']
    user = User()
    user.create(email=email, password=password)
    return jsonify(user.serialize()), 201


@app.route('/css')
def return_css():
    return url_for('static', filename='style.css')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
