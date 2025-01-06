from enums.level import LEVEL

class User:
    def __init__(self, username='', email='', password='', level: LEVEL = None):
        self.username = username
        self.email = email
        self.password = password
        self.level = level