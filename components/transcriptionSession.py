from abc import ABC, abstractmethod
from datetime import time

from flask import jsonify
from enums.dialect import Dialect
from components.dialect_management import DialectManagement
import speech_recognition as sr
from enums.mode import Mode
from imp.dialectManagementImp import DialectManagementImpl

class TranscriptionSession(ABC):
    # makes possible dependency injection
    def __init__(self, mode: Mode, dialect_manager : DialectManagementImpl):
        self.start_time = None
        self.end_time = None
        self.mode = mode
        self.status = False
        self.dialect_manager = dialect_manager
        self.recognizer = sr.Recognizer()

    @abstractmethod
    def startTranscription(self):
        self.status = True
        self.start_time = time.time()

        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source)
            print("Start speaking...")
            audio = self.recognizer.listen(source)

        transcription = self.recognizer.recognize_google(audio, language='sq')
        print("Transcription: ", transcription)
        
        return transcription

    @abstractmethod
    def endTranscription(self):
        self.status = False
        self.end_time = time.time()

    @abstractmethod
    def pauseTranscription(self):
        self.status = False

    @abstractmethod
    def resumeTranscription(self):
        self.status = True

    @abstractmethod
    def saveTranscription(self, transcription, filename="transcription.txt"):
        with open(filename, 'w') as file:
            file.write(transcription)

    @abstractmethod
    def manageTranscriptionAudio(self, audio):
        dialect = self.dialect_manager.detectDialect(audio)
        self.dialect_manager.applyDialectRules(dialect)

    @abstractmethod
    def detectDialect(self, audioInput) -> Dialect:
        return super().detect_dialect(audioInput)

    @abstractmethod
    def applyDialectRules(self, dialect: Dialect):
        pass