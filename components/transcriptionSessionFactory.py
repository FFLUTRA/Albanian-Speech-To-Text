from components.mode import Mode
from components.singleSession import SingleSession
from components.collaborationSession import CollaborationSession
from components.transcriptionSession import TranscriptionSession

class TranscriptionSessionFactory:
    @staticmethod
    def create_transcription_session(mode: Mode, user_id=None, admin_id=None):
        if mode == Mode.ONLINE:
            if admin_id is not None:
                return CollaborationSession(mode, admin_id)
            elif user_id is not None:
                return SingleSession(mode, user_id)
            else:
                raise ValueError("Either admin_id or user_id must be provided for ONLINE mode.")
            
        elif mode == Mode.OFFLINE:
            return SingleSession(mode, user_id)
        else:
            raise ValueError("Invalid mode provided. Supported modes are ONLINE and OFFLINE.")