from datetime import time

from flask import flash
from enums.dialect import Dialect
from enums.mode import Mode
from components.transcriptionSession import TranscriptionSession
from components.dialect_management import DialectManagement
import speech_recognition as sr

from imp.dialectManagementImp import DialectManagementImpl


class SingleSession(TranscriptionSession):
    def __init__(self, mode: Mode, dialect_manager: DialectManagementImpl, user_id: int):
        super().__init__(mode, dialect_manager)
        self.user_id = user_id

    def startTranscription(self):
        return super().startTranscription()

    def endTranscription(self):
        super().endTranscription()
    
    def saveTranscription(self):
        super().saveTranscription()

    def pauseTranscription(self):
        super().pauseTranscription()

    def resumeTranscription(self):
        super().resumeTranscription()
        
    def manageTranscriptionAudio(self, audio) -> Dialect:
        super().manageTranscriptionAudio(audio)
    
    def detectDialect(audio):
        return super().manageTranscriptionAudio(audio)

    def applyDialectRules(self, dialect: Dialect):
        super().applyDialectRules()