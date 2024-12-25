import psycopg2
import secrets
from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from passlib.hash import sha1_crypt
from DAOs.userDAO import UserDao
from messages import LOGIN_SUCCESS, LOGIN_FAIL, REGISTER_SUCCESS, REGISTER_FAIL
from components.user import User
from components.feedback import Feedback
from components.presentation_manager import PresentationManager
import speech_recognition as sr


app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
presentation_manager = PresentationManager()

presentation_manager.start()

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
   
    flash('Please log in to access your profile.', 'error')
    return redirect(url_for('login'))

def db_conn():
    conn = psycopg2.connect(database="astt_db", host="localhost", user="postgres", password="postgres", port="5432")
    return conn

@app.route('/create', methods=['POST'])
def createUser():
    username = request.form['username']
    email = request.form['email']
    password = sha1_crypt.hash(request.form['password'])
    level = request.form['security_level']
    user = User(username, email, password, level)

    user_dao = UserDao()

    if user_dao.add_user(user):
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
        stored_hash = user_data[3]
        if sha1_crypt.verify(password, stored_hash):
            return True  
    return False  

@app.route('/login', methods=['GET', 'POST'])
def login_user():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if validate_login(email, password):
            session['user_email'] = email
            flash(LOGIN_SUCCESS, 'success')

            return render_template('index.html')
       
        flash(LOGIN_FAIL, 'error')
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

        user_dao = UserDao()
        if user_dao.update_email(User(email=current_email), new_email):
            flash('Email updated successfully.', 'success')
            return redirect(url_for('logout'))
        else:
            flash('Error updating email.', 'error')

        return redirect(url_for('profile'))

    flash('Please log in to access your profile.', 'error')
    return render_template('profile.html')

@app.route('/update_password', methods=['POST'])
def update_password():
    if 'user_email' in session:
        current_email = session['user_email']
        new_password = request.form['new_password']

        if not new_password:
            flash('New password cannot be empty.', 'error')
            return redirect(url_for('profile'))

        user_dao = UserDao()    
        if user_dao.reset_password(User(email=current_email), new_password):
            flash('Password updated successfully.', 'success')
            return redirect(url_for('logout'))
        else:
            flash('Error updating password.', 'error')

        return redirect(url_for('profile'))

    flash('Please log in to access your profile.', 'error')
    return render_template('profile.html')

@app.route('/update_level', methods=['POST'])
def update_level():
    if 'user_email' in session:
        current_email = session['user_email']
        new_level = request.form['new_level']

        if not new_level:
            flash('New level cannot be empty.', 'error')
            return redirect(url_for('profile'))

        user_dao = UserDao()

        if user_dao.update_security_level(User(email=current_email), new_level):
            flash('Level updated successfully.', 'success')
        else:
            flash('Error updating level.', 'error')

        return redirect(url_for('profile'))

    flash('Please log in to access your profile.', 'error')
    return render_template('profile.html')

@app.route('/delete_account', methods=['POST'])
def delete_account():
    if 'user_email' in session:
        current_email = session['user_email']
       
        user_dao = UserDao()    

        if user_dao.delete_account(User(email=current_email)):
            session.pop('user_email', None)
            flash('Account deleted successfully.', 'success')
            return redirect(url_for('home'))
        else:
            flash('Error deleting account.', 'error')
            return redirect(url_for('profile'))

    flash('Please log in to access your profile.', 'error')
    return render_template('profile.html')

@app.route('/logout')
def logout():
    session.pop('user_email', None)

    return redirect(url_for('home'))

def get_user_id_by_email(email):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute("SELECT id FROM users WHERE email = %s", (email,))
    user_id = cur.fetchone()
    cur.close()
    conn.close()

    if user_id:
        return user_id[0]  

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


recognizer = sr.Recognizer()

@app.route('/transcription', methods=['GET', 'POST'])
def transcription():
    global recognizer
    if request.method == 'POST':
        if 'audio' in request.files:
            audio_data = request.files['audio'].read()
            try:
                with sr.AudioFile(audio_data) as source:
                    audio_text = recognizer.recognize_google(source)
                return jsonify({'transcription': audio_text})
            except sr.UnknownValueError:
                return jsonify({'error': 'Speech Recognition could not understand the audio'})
            except sr.RequestError as e:
                return jsonify({'error': f"Could not request results from Google Speech Recognition service; {e}"})
        else:
            return jsonify({'error': 'No audio file provided'})
    return render_template('transcription.html')

@app.route('/my_feedbacks')
def my_feedbacks():
    if 'user_email' in session:
        email = session['user_email']
        user_id = get_user_id_by_email(email)

        if user_id is not None:
            feedback_instance = Feedback(user_id, None)
            feedback_data = feedback_instance.get_feedbacks_by_user_id()
            return render_template('my_feedbacks.html', data=feedback_data)

    flash('Please log in to access your feedbacks.', 'error')
    return redirect(url_for('login'))


 
if __name__ == '__main__':
    presentation_manager.modeManager()
    app.run(debug=True)
