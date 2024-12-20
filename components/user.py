from typing import Type
from components.level import LEVEL


class User:
    def __init__(self, username='', email='', password='', level: Type[LEVEL] = None):
        self.username = username
        self.email = email
        self.password = password
        self.level = level