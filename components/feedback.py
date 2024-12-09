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

    def read_feedback(self, message_id):
        conn = self.db_conn.connect()

        try:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM messages WHERE id = %s", (message_id,))
                message = cur.fetchone()
                return message
        finally:
            conn.close()

    def readAll_feedback(self):
        conn = self.db_conn.connect()

        try:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM messages")
                message = cur.fetchone()
                return message
        finally:
            conn.close()        

    def update_feedback(self, message_id, updated_feedback_data):
        conn = self.db_conn.connect()

        try:
            with conn.cursor() as cur:
                cur.execute("UPDATE messages SET feedback_data = %s WHERE id = %s", (updated_feedback_data, message_id))
                conn.commit()
                flash("Message updated successfully!", 'success')
        except Exception as e:
            conn.rollback()
            flash(f"Error updating the message: {str(e)}", 'error')
        finally:
            conn.close()

    def delete_feedback(self, message_id):
        conn = self.db_conn.connect()

        try:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM messages WHERE id = %s", (message_id,))
                conn.commit()
                flash("Message deleted successfully!", 'success')
        except Exception as e:
            conn.rollback()
            flash(f"Error deleting the message: {str(e)}", 'error')
        finally:
            conn.close()