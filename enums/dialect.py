from enum import Enum

class Dialect(Enum):
    STANDARD = "STANDARD"
    GEGE = "GEGE"
    TOSKE = "TOSKE"

    def default():
        return Dialect.STANDARD