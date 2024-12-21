from datetime import time
from components.mode import Mode
from components.transcriptionSession import TranscriptionSession


class SingleSession(TranscriptionSession):
    def __init__(self, mode: Mode, user_id: int):
        super().__init__(mode)
        self.user_id = user_id

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