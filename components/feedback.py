from components.dbconn import DbConn

class Feedback:
    def __init__(self, user_id='', feedback_data=''):
        self.user_id = user_id
        self.feedback_data = feedback_data