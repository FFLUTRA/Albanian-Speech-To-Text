from abc import ABC, abstractmethod
from components.mode import Mode

class TranscriptionSession(ABC):
    def __init__(self, mode: Mode):
        self.start_time = None
        self.end_time = None
        self.mode = mode
        self.transcription_in_progress = False
        self.paused = False

    @abstractmethod
    def startTranscription(self):
        pass

    @abstractmethod
    def endTranscription(self):
        pass

    @abstractmethod
    def pauseTranscription(self):
        pass

    @abstractmethod
    def resumeTranscription(self):
        pass