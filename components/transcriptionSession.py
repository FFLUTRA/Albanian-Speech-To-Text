from abc import ABC, abstractmethod
from components.dialect import Dialect
from components.dialect_management import DialectManagement
from components.mode import Mode

class TranscriptionSession(ABC):
    # makes possible dependency injection
    def __init__(self, mode: Mode, dialect_manager: DialectManagement):
        self.start_time = None
        self.end_time = None
        self.mode = mode
        self.transcription_in_progress = False
        self.paused = False
        self.dialect_manager = dialect_manager

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