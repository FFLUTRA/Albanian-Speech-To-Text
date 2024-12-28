from abc import ABC, abstractmethod
from flask import flash
import speech_recognition as sr

from components.dialect import Dialect
from components.dialect_management import DialectManagement

class DialectManagementImpl(DialectManagement):

    def detectDialect(self, audioInput) -> Dialect:
        return super().detectDialect()


    def applyDialectRules(self, dialect: Dialect):
        return super().applyDialectRules()



