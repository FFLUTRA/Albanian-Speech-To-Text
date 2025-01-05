from abc import ABC, abstractmethod
from flask import flash
import speech_recognition as sr

from enums.dialect import Dialect

class DialectManagement(ABC):
    
    @abstractmethod
    def detectDialect(self, audioInput) -> Dialect:
        pass

    @abstractmethod
    def applyDialectRules(self, dialect: Dialect):
        pass