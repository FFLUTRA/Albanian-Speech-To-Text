import psycopg2

conn = psycopg2.connect(database="astt_db", host="localhost", user="postgres", password="postgres", port="5432")
cur = conn.cursor()

cur.execute('''CREATE TYPE level AS ENUM ('LOW', 'MEDIUM', 'HIGH')''')
cur.execute('''CREATE TABLE IF NOT EXISTS users (id serial PRIMARY KEY, username varchar(100), email varchar(255), password varchar(255), level level)''')
cur.execute('''INSERT INTO users (username, email, password, level) VALUES ('flutramusaj', 'flutramusaj0@gmail.com', 'flutra000', 'HIGH'::level)''')

conn.commit()
cur.close()
conn.close()
