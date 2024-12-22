from abc import ABC, abstractmethod
import audioop
from dialect import Dialect

class DialectManagement(ABC):
    @abstractmethod
    def detectDialect(self, audioInput: audioop) -> Dialect:
        pass

    @abstractmethod
    def applyDialectRules(self, dialect: Dialect):
        pass