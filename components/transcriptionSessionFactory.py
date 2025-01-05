from components.dialect_management import DialectManagement
from enums.mode import Mode
from components.singleSession import SingleSession
from components.collaborationSession import CollaborationSession

class TranscriptionSessionFactory: #Simple Factory 
#     @staticmethod
#     def create_transcription_session(self, mode: Mode, dialect_manager: DialectManagement, user_id=None, admin_id=None):
        # if admin_id is not None:
        #     return CollaborationSession(mode, admin_id, dialect_manager)
        # elif user_id is not None:
        #     return SingleSession(mode, user_id, dialect_manager)         

    session_creation_map = {
        (True, False): CollaborationSession,
        (False, True): SingleSession
    }

    @staticmethod
    def _get_session_type(is_admin, is_user):
        # Lazy loading
        return TranscriptionSessionFactory.session_creation_map.get((is_admin, is_user), None)

    @staticmethod
    def create_transcription_session(mode: Mode, dialect_manager: DialectManagement, user_id=None, admin_id=None):
        is_admin = admin_id is not None
        is_user = user_id is not None

        # Lazy loading
        session_type = TranscriptionSessionFactory._get_session_type(is_admin, is_user)

        if session_type:
            # RIP
            return session_type(mode, admin_id or user_id, dialect_manager)