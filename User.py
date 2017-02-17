import uuid

import bcrypt
import re


class User(object):
    MINIMUM_PASSWORD_LENGTH = 8
    EMAIL_PATTERN = r"[^@]+@[^@]+\.[^@]+"

    def __init__(self):
        self.id = None
        self.password = None
        self.email = None

    def create(self, password, email):
        self.id = uuid.uuid4()
        self.set_password(password=password)
        self.set_email(email=email)

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
