import bcrypt
import re
from flask import Flask, request, jsonify, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class User(db.Model):
    MINIMUM_PASSWORD_LENGTH = 8
    EMAIL_PATTERN = r"[^@]+@[^@]+\.[^@]+"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120))
    password = db.Column(db.String(80))

    def __init__(self, email, password):
        self.set_email(email=email)
        self.set_password(password=password)

    def __repr__(self):
        return '<User %r>' % self.username

    def set_password(self, password):
        if len(password) >= User.MINIMUM_PASSWORD_LENGTH:
            self.password = str(bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode())

    def set_email(self, email):
        if re.match(User.EMAIL_PATTERN, email):
            self.email = email

    def serialize(self):
        return {
            'id': self.id,
            'email': self.email,
            'password': self.password,
        }


@app.route('/')
def hello_world():
    return "hello, world"


@app.route('/api/v0/users', methods=['POST'])
def create_user():
    email = request.json['email']
    password = request.json['password']
    user = User(email, password)
    return jsonify(user.serialize()), 201


@app.route('/css')
def return_css():
    return url_for('static', filename='style.css')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
