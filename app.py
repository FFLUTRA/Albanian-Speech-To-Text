import psycopg2
import secrets
from flask import Flask, render_template, request, redirect, url_for, session
from passlib.hash import sha1_crypt
from messages import LOGIN_SUCCESS, LOGIN_FAIL, REGISTER_SUCCESS, REGISTER_FAIL
from components.user import User
from flask import flash
from components.feedback import Feedback

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

@app.route('/profile')
def profile():
    if 'user_email' in session:
        email = session['user_email']
        conn = db_conn()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE email = %s", (email,))
        user_data = cur.fetchone()
        cur.close()
        conn.close()

        if user_data:
            return render_template('profile.html', user_data=user_data)
   
    # Redirect to login if the user is not logged in
    flash('Please log in to access your profile.', 'error')
    return redirect(url_for('login'))

def db_conn():
    conn = psycopg2.connect(database="astt_db", host="localhost", user="postgres", password="postgres", port="5432")
    return conn

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

def get_username_by_email(email):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute("SELECT username FROM users WHERE email = %s", (email,))
    username = cur.fetchone()
    cur.close()
    conn.close()

    if username:
        return username

def get_password_by_email(email):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute("SELECT password FROM users WHERE email = %s", (email,))
    password = cur.fetchone()
    cur.close()
    conn.close()

    if password:
        return password
   
def get_level_by_email(email):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute("SELECT level FROM users WHERE email = %s", (email,))
    level = cur.fetchone()
    cur.close()
    conn.close()

    if level:
        return level

@app.route('/update_email', methods=['POST'])
def update_email():
    if 'user_email' in session:
        current_email = session['user_email']
        new_email = request.form['new_email']

        if not new_email:
            flash('New email cannot be empty.', 'error')
            return redirect(url_for('profile'))

        # Create an instance of the User class
        user = User(username=get_username_by_email(current_email), email=current_email, password=get_username_by_email(current_email), level=get_level_by_email(current_email))
   
        # Call the updateEmail method
        if user.updateEmail(new_email):
            flash('Email updated successfully.', 'success')
        else:
            flash('Error updating email.', 'error')

        return redirect(url_for('profile'))

    flash('Please log in to access your profile.', 'error')
    return render_template('profile.html')

# @app.route('/update_email', methods=['POST'])
# def update_password():
#     if 'user_email' in session:
#         current_email = session['user_email']
#         new_email = request.form['new_email']

#         if not new_email:
#             flash('New email cannot be empty.', 'error')
#             return redirect(url_for('profile'))

#         # Create an instance of the User class
#         user = User(username=get_username_by_email(current_email), email=current_email, password=get_username_by_email(current_email), level=get_level_by_email(current_email))
   
#         # Call the updateEmail method
#         if user.updateEmail(new_email):
#             flash('Email updated successfully.', 'success')
#         else:
#             flash('Error updating email.', 'error')

#         return redirect(url_for('profile'))

#     flash('Please log in to access your profile.', 'error')
#     return render_template('profile.html')

@app.route('/update_level', methods=['POST'])
def update_level():
    if 'user_email' in session:
        current_email = session['user_email']
        new_level = request.form['new_level']

        if not new_level:
            flash('New level cannot be empty.', 'error')
            return redirect(url_for('profile'))

        # Create an instance of the User class
        user = User(username=get_username_by_email(current_email), email=current_email, password=get_username_by_email(current_email), level=get_level_by_email(current_email))
   
        if user.updateSecurityLevel(new_level):
            flash('Level updated successfully.', 'success')
        else:
            flash('Error updating level.', 'error')

        return redirect(url_for('profile'))

    flash('Please log in to access your profile.', 'error')
    return render_template('profile.html')

@app.route('/logout')
def logout():
    # Clear the user session data
    session.pop('user_email', None)

    # Redirect to the home page or any desired route after logout
    return redirect(url_for('home'))

def get_user_id_by_email(email):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute("SELECT id FROM users WHERE email = %s", (email,))
    user_id = cur.fetchone()
    cur.close()
    conn.close()

    if user_id:
        return user_id[0]  # Assuming user_id is the first column, adjust as needed

    return None

def index():
    if request.method == 'POST':
        if 'user_email' in session:
            email = session['user_email']
            feedback_data = request.form['message']
            user_id = get_user_id_by_email(email)
            feedback = Feedback(user_id, feedback_data)

            if user_id is not None:
                feedback.submit_feedback(user_id, feedback_data)
                flash("Message submitted successfully!", 'success')
                return redirect(url_for('index'))
    return redirect(url_for('index'))
                   
@app.route('/submit_contact', methods=['POST'])
def submit_feedback():
    if 'user_email' in session:
        email = session['user_email']
        feedback_data = request.form['message']
        user_id = get_user_id_by_email(email)
        feedback = Feedback(user_id, feedback_data)

        if user_id is not None:
            feedback.submit_feedback(user_id, feedback_data)
            flash("Message submitted successfully!", 'success')
            return redirect(url_for('contact'))
    return redirect(url_for('contact'))

@app.route('/messages')
def messages():
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('''SELECT * FROM messages''')
    data = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('messages.html', data = data)


@app.route('/users')
def index():
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('''SELECT * FROM users''')
    data = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('users.html', data = data)
 
if __name__ == '__main__':
    app.run(debug=True)
