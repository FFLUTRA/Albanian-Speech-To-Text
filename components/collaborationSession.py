from datetime import time
from components.dialect import Dialect
from components.mode import Mode
from components.transcriptionSession import TranscriptionSession


class CollaborationSession(TranscriptionSession):
    def __init__(self, mode: Mode, admin_id: int):
        super().__init__(mode)
        self.users = []
        self.admin_id = admin_id

    def startTranscription(self):
        if not self.transcription_in_progress:
            self.start_time = time.time()
            self.transcription_in_progress = True
            # SpechRec = SpeechRecognition()
            # Code that will directly interect with our SpeechRecognition will be implementet here

    def endTranscription(self):
        if self.transcription_in_progress:
            self.end_time = time.time()
            self.transcription_in_progress = False
            self.paused = False

    def pauseTranscription(self):
        if self.transcription_in_progress and not self.paused:
            self.paused = True

    def resumeTranscription(self):
        if self.transcription_in_progress and self.paused:
            self.paused = False

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
    
    def detect_dialect(audio):
        return super().manageTranscriptionAudio(audio)

    def applyDialectRules(self, dialect: Dialect):
        # Logic that will be based on albanian datasets the will be created soon
        pass