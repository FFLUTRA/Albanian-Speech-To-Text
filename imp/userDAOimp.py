from passlib.hash import sha1_crypt
from DAOs.userDAO import UserDao
from components.dbconn import DbConn
from components.level import LEVEL
from components.user import User


class UserDaoImplementation(UserDao):

    def __init__(self):
        self.db_conn = DbConn()

    def add_user(self, user: User) :
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

    def update_email(self, user:User, new_email:str):
        conn = self.db_conn.connect()

        try:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM users WHERE email = %s", (user.email,))
                existing_user = cur.fetchone()

                if existing_user:
                    cur.execute("UPDATE users SET email = %s WHERE email = %s", (new_email, user.email))
                    conn.commit()
                    return True
                else:
                    return False
        finally:
            conn.close()  

    def reset_password(self, user, new_password):
        conn = self.db_conn.connect()

        try:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM users WHERE email = %s", (user.email,))
                existing_user = cur.fetchone()

                if existing_user:
                    new_hashed_password = sha1_crypt.hash(new_password)
                    cur.execute("UPDATE users SET password = %s WHERE email = %s", (new_hashed_password, user.email))
                    conn.commit()
                    return True
                else:
                    return False
        finally:
            conn.close()