import psycopg2

class DbConn:
    def __init__(self, database="astt_db", host="localhost", user="postgres", password="postgres", port="5432"):
    # def __init__(self, database = , host, user, password, port):
        self.database = database
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.conn = None
        self.cur = None

    def connect(self):
        try:
            self.conn = psycopg2.connect(
                database=self.database,
                host=self.host,
                user=self.user,
                password=self.password,
                port=self.port
            )
            self.cur = self.conn.cursor()
            return self.conn
        except Exception as e:
            print(f"Error: Unable to connect to the database. {e}")

    def disconnect(self):
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()
            print("Disconnected from the database.")

    def commit(self):
        if self.conn:
            self.conn.commit()
            print("Changes committed.")
