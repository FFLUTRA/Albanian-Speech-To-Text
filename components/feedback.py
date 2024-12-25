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

    def get_feedbacks_by_user_id(self):
        conn = self.db_conn.connect()

        try:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM messages WHERE user_id = %s", (self.user_id,))
                data = cur.fetchall()
        finally:
            conn.close()

        return data

    # def read_feedback(self, message_id):
    #     conn = self.db_conn.connect()

    #     try:
    #         with conn.cursor() as cur:
    #             cur.execute("SELECT * FROM messages WHERE id = %s", (message_id,))
    #             message = cur.fetchone()
    #             return message
    #     finally:
    #         conn.close()

    # def readAll_feedback(self):
    #     conn = self.db_conn.connect()

    #     try:
    #         with conn.cursor() as cur:
    #             cur.execute("SELECT * FROM messages")
    #             message = cur.fetchone()
    #             return message
    #     finally:
    #         conn.close()        
    # def update_feedback(self, feedback_id, updated_message):
    #     conn = self.db_conn.connect()

    #     try:
    #         with conn.cursor() as cur:
    #             cur.execute("UPDATE messages SET feedback_data = %s WHERE feedback_data = %s", (updated_message, self.feedback_data))
    #             conn.commit()
    #     finally:
    #         conn.close()

    # def delete_feedback(self, feedback_id):
    #     conn = self.db_conn.connect()

    #     try:
    #         with conn.cursor() as cur:
    #             cur.execute("DELETE FROM messages WHERE feedback_id = %s", (feedback_id,))
    #             conn.commit()
    #     finally:
    #         conn.close()

    # def get_feedback_data():
    #     db_conn = DbConn(database="astt_db", host="localhost", user="postgres", password="postgres", port="5432")
    #     conn = db_conn.connect()

    #     try:
    #         with conn.cursor() as cur:
    #             cur.execute("SELECT * FROM messages ORDER BY submission_date DESC")
    #             data = cur.fetchall()
    #     finally:
    #         conn.close()

    #     return data