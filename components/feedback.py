from flask import flash
from components.dbconn import DbConn

class Feedback:
    def __init__(self, user_id, feedback_data):
        self.user_id = user_id
        self.feedback_data = feedback_data
        self.db_conn = DbConn(database="astt_db", host="localhost", user="postgres", password="postgres", port="5432")

    def submit_feedback(self, user_id, feedback_data):
        user_id = self.user_id
        feedback_data = self.feedback_data
        conn = self.db_conn.connect()

        try:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO messages (user_id, feedback_data, submission_date) VALUES (%s, %s, CURRENT_TIMESTAMP)",
                        (user_id, feedback_data))
                conn.commit()
        finally:
            conn.close()