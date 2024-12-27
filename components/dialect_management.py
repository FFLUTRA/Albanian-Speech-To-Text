from abc import ABC, abstractmethod
from dialect import Dialect

class DialectManagement(ABC):
    @abstractmethod
    def detectDialect(self, audioInput) -> Dialect:
        pass

    @abstractmethod
    def applyDialectRules(self, dialect: Dialect):
        pass