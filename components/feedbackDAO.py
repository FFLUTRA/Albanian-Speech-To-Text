# from components.dbconn import DbConn

# class FeedbackDAO:
#     def __init__(self):
#         self.db_conn = DbConn()
    
#     def submit_feedback(self, user_id, feedback_data):
#         user_id = self.user_id
#         feedback_data = self.feedback_data
#         conn = self.db_conn.connect()

#         try:
#             with conn.cursor() as cur:
#                 cur.execute("INSERT INTO messages (user_id, feedback_data, submission_date) VALUES (%s, %s, CURRENT_TIMESTAMP)",
#                         (user_id, feedback_data))
#                 conn.commit()
#         finally:
#             conn.close(