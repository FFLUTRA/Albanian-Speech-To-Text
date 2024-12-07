# messages.py

import psycopg2
from flask import flash

def db_conn():
    return psycopg2.connect(database="astt_db", host="localhost", user="postgres", password="postgres", port="5432")

def submit_message(user_id, message_text):
    conn = db_conn()
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO messages (user_id, feedback_data, submission_date) VALUES (%s, %s, CURRENT_TIMESTAMP)",
                    (user_id, message_text))
        conn.commit()
        flash("Message submitted successfully!", 'success')
    except Exception as e:
        conn.rollback()
        flash(f"Error submitting the message: {str(e)}", 'error')
    finally:
        cur.close()
        conn.close()