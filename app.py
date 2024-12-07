import psycopg2
import secrets
from flask import Flask, render_template, request, redirect, url_for, session
from passlib.hash import sha1_crypt
from messages import LOGIN_SUCCESS, LOGIN_FAIL, REGISTER_SUCCESS, REGISTER_FAIL
from components.user import User
from flask import flash

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

def db_conn():
    conn = psycopg2.connect(database="astt_db", host="localhost", user="postgres", password="postgres", port="5432")
    return conn

def validate_login(email, password):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE email = %s", (email,))
    user_data = cur.fetchone()
    cur.close()
    conn.close()

    if user_data:
        stored_hash = user_data[3]  # Assuming the hash is stored in the 4th column, adjust as needed
        if sha1_crypt.verify(password, stored_hash):
            return True  # Password is correct
    return False  # Invalid email or password

# Route for login
@app.route('/login', methods=['GET', 'POST'])
def login_user():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Validate login credentials
        if validate_login(email, password):
            # Set the user as logged in (you can use a session or other authentication mechanisms)
            session['user_email'] = email
            flash(LOGIN_SUCCESS, 'success')

            # Redirect to the homepage or any desired route after successful login
            return redirect(url_for('index'))
       
        flash(LOGIN_FAIL, 'error')
        # If login fails, you can render an error message or redirect back to the login page
        return render_template('login.html', error='Invalid email or password')
       

    return render_template('login.html')

@app.route('/')
def index():
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('''SELECT * FROM users''')
    data = cur.fetchall();
    cur.close();
    conn.close();
    return render_template('index.html', data = data)

@app.route('/create', methods=['POST'])
def createUser():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    level = request.form['security_level']
    user = User(username, email, password, level)

    if user.add_user():
        flash(REGISTER_SUCCESS, 'success')
        return render_template('login.html')
   
    flash(REGISTER_FAIL, 'error')
    return render_template('register.html')

@app.route('/logout')
def logout():
    # Clear the user session data
    session.pop('user_email', None)

    # Redirect to the home page or any desired route after logout
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)