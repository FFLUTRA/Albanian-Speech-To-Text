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
        return super().endTranscription()
    
    def saveTranscription(self):
        return super().saveTranscription()

    def pauseTranscription(self):
        if self.transcription_in_progress and not self.paused:
            self.paused = True

    def resumeTranscription(self):
        if self.transcription_in_progress and self.paused:
            self.paused = False
        
    def manageTranscriptionAudio(self, audio) -> Dialect:
        return super().manageTranscriptionAudio(audio)
    
    def detectDialect(audio):
        return super().manageTranscriptionAudio(audio)

    def applyDialectRules(self, dialect: Dialect):
        return super().applyDialectRules()