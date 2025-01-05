from datetime import time
from enums.dialect import Dialect
from components.dialect_management import DialectManagement
from enums.mode import Mode
from components.transcriptionSession import TranscriptionSession


class CollaborationSession(TranscriptionSession):
    def __init__(self, mode: Mode, dialect_manager: DialectManagement, admin_id: int):
        super().__init__(mode, dialect_manager)
        self.users = []
        self.admin_id = admin_id

    def startTranscription(self):
        return super().startTranscription()

    def endTranscription(self):
        return super().startTranscription()

    def pauseTranscription(self):
        if self.transcription_in_progress and not self.paused:
            self.paused = True

    def resumeTranscription(self):
        if self.transcription_in_progress and self.paused:
            self.paused = False
        
    def saveTranscription(self):
        return super().saveTranscription()

    def inviteParticipant(self, user_id):
        if user_id in self.users:
            return False

        self.users.append(user_id)
        return True
    
    def removeParticipant(self, user_id):
        if user_id == self.admin_id:
            return False

        if user_id in self.users:
            self.users.remove(user_id)
            return True
        else:
            return False
        
    def leaveSession(self, user_id):
        if user_id == self.admin_id:
            self.endTranscription()
            return True
        
        if user_id in self.users:
            self.users.remove(user_id)
            return True
        else:
            return False
        
    def manageTranscriptionAudio(self, audio) -> Dialect:
        return super().manageTranscriptionAudio(audio)
    
    def detectDialect(audio):
        return super().manageTranscriptionAudio(audio)

    def applyDialectRules(self, dialect: Dialect):
        return super().applyDialectRules()