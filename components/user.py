import psycopg2
from passlib.hash import sha1_crypt
from components.dbconn import DbConn 

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
                cur.execute("INSERT INTO users(username, email, password, level) VALUES(%s, %s, %s, %s)", (username, email, password, level))
                conn.commit()
        finally:
            conn.close()