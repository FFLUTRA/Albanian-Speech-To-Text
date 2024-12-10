from flask import flash
import psycopg2
from passlib.hash import sha1_crypt
from components.dbconn import DbConn
from messages import REGISTER_FAIL, REGISTER_SUCCESS 

class User:
    def __init__(self, username='', email='', password='', level=''):
        self.username = username
        self.email = email
        self.password = password
        self.level = level
        self.db_conn = DbConn(database="astt_db", host="localhost", user="postgres", password="postgres", port="5432")

    def add_user(self):
        username = self.username
        email = self.email
        password = sha1_crypt.hash(self.password)
        level = self.level

        conn = self.db_conn.connect()

        try:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM users WHERE email = %s", (email,))
                existing_user = cur.fetchone()

                if existing_user:
                    return False
                else:
                    cur.execute("INSERT INTO users(username, email, password, level) VALUES(%s, %s, %s, %s)", (username, email, password, level))
                    conn.commit()
                    return True
        finally:
            conn.close()
    
    def updateEmail(self, new_email):
        conn = self.db_conn.connect()

        try:
            with conn.cursor() as cur:
                cur.execute("UPDATE users SET email = %s WHERE email = %s", (new_email, self.email))
                conn.commit()
                return True
        finally:
            conn.close()

    def resetPassword(self, new_password):
        conn = self.db_conn.connect()

        try:
            with conn.cursor() as cur:
                new_hashed_password = sha1_crypt.hash(new_password)
                cur.execute("UPDATE users SET password = %s WHERE username = %s", (new_hashed_password, self.username))
                conn.commit()
                return True
        finally:
            conn.close()

    def updateSecurityLevel(self, new_level):
        conn = self.db_conn.connect()

        try:
            with conn.cursor() as cur:
                cur.execute("UPDATE users SET level = %s WHERE email = %s", (new_level, self.email))
                conn.commit()
                return True
        finally:
            conn.close()

    def deleteAccount(self):
        conn = self.db_conn.connect()

        try:
            with conn.cursor() as cur:
                # Get the user ID
                cur.execute("SELECT id FROM users WHERE email = %s", (self.email,))
                user_id = cur.fetchone()

                if user_id:
                    user_id = user_id[0]
                    # Delete user messages
                    cur.execute("DELETE FROM messages WHERE user_id = %s", (user_id,))

                    # Delete user
                    cur.execute("DELETE FROM users WHERE email = %s", (self.email,))
                    
                    conn.commit()
                    return True
                else:
                    return False
        finally:
            conn.close()