from typing import Type
from passlib.hash import sha1_crypt
from components.dbconn import DbConn
from components.level import LEVEL
from components.user import User

class UserDao:
    def __init__(self):
        self.db_conn = DbConn(database="astt_db", host="localhost", user="postgres", password="postgres", port="5432")

    def add_user(self, user):
        conn = self.db_conn.connect()

        try:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM users WHERE email = %s", (user.email,))
                existing_user = cur.fetchone()

                if existing_user:
                    return False
                else:
                    cur.execute("INSERT INTO users(username, email, password, level) VALUES(%s, %s, %s, %s)",
                                (user.username, user.email, user.password, user.level))
                    conn.commit()
                    return True
        finally:
            conn.close()

    def update_email(self, user, new_email):
        conn = self.db_conn.connect()

        try:
            with conn.cursor() as cur:
                cur.execute("UPDATE users SET email = %s WHERE email = %s", (new_email, user.email))
                conn.commit()
                return True
        finally:
            conn.close()


    def reset_password(self, user, new_password):
        conn = self.db_conn.connect()

        try:
            with conn.cursor() as cur:
                new_hashed_password = sha1_crypt.hash(new_password)
                cur.execute("UPDATE users SET password = %s WHERE email = %s", (new_hashed_password, user.email))
                conn.commit()
                return True
        finally:
            conn.close()

    def update_security_level(self, user, new_level):
        conn = self.db_conn.connect()

        try:
            with conn.cursor() as cur:
                cur.execute("UPDATE users SET level = %s WHERE email = %s", (new_level, user.email))
                conn.commit()
                return True
        finally:
            conn.close()

    def delete_account(self, user):
        conn = self.db_conn.connect()

        try:
            with conn.cursor() as cur:
                cur.execute("SELECT id FROM users WHERE email = %s", (user.email,))
                user_id = cur.fetchone()

                if user_id:
                    user_id = user_id[0]
                    cur.execute("DELETE FROM messages WHERE user_id = %s", (user_id,))
                    cur.execute("DELETE FROM users WHERE email = %s", (user.email,))
                    conn.commit()
                    return True
                else:
                    return False
        finally:
            conn.close()

    def get_user_details(self, user_id):
        conn = self.db_conn.connect()

        try:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM users WHERE id = %s", (user_id,))
                user_data = cur.fetchone()

                if user_data:
                    username, email, password, level = user_data
                    return User(username=username, email=email, password=password, level=level)

        finally:
            conn.close()