from components.dialect_management import DialectManagement
from components.mode import Mode
from components.singleSession import SingleSession
from components.collaborationSession import CollaborationSession
from components.transcriptionSession import TranscriptionSession

class TranscriptionSessionFactory:
    @staticmethod
    def create_transcription_session(self, mode: Mode, user_id: int, dialect_manager: DialectManagement):
        if mode == Mode.SINGLE:
            return SingleSession(mode, user_id, dialect_manager)
        elif mode == Mode.COLLABORATION:
            return CollaborationSession(mode, user_id, dialect_manager)
            
        elif mode == Mode.OFFLINE:
            return SingleSession(mode, user_id)
        else:
            raise ValueError("Invalid mode provided. Supported modes are ONLINE and OFFLINE.")