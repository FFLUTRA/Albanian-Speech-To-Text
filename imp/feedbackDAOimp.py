from DAOs.feedbackDAO import FeedbackDAO
from components.dbconn import DbConn

class FeedbackDaoImplementation(FeedbackDAO):
    def __init__(self):
        self.db_conn = DbConn()

    def submit_feedback(self, feedback):
        conn = self.db_conn.connect()

        try:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO messages (user_id, feedback_data, submission_date) VALUES (%s, %s, CURRENT_TIMESTAMP)",
                            (feedback.user_id, feedback.feedback_data,))
                conn.commit()
        finally:
            conn.close()

    def get_feedbacks_by_user_id(self, feedback):
        conn = self.db_conn.connect()

        try:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM messages WHERE user_id = %s", (feedback.user_id,))
                data = cur.fetchall()
        finally:
            conn.close()

        return data
    
    def update_feedback(self, feedback_id, feedback_data):
        conn = self.db_conn.connect()

        try:
            with conn.cursor() as cur:
                cur.execute("UPDATE messages SET feedback_data = %s WHERE feedback_id = %s", (feedback_data, feedback_id,))
                conn.commit()
        finally:
            conn.close()

    def delete_feedback(self, feedback_id):
        conn = self.db_conn.connect()

        try:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM messages WHERE feedback_id = %s", (feedback_id,))
                conn.commit()
        finally:
            conn.close()