from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your_email@gmail.com'
app.config['MAIL_PASSWORD'] = 'your_password'

mail = Mail(app)
login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin):
    # This is a simplified example; in a real app, you'd have a database model here.
    def __init__(self, id, username, email):
        self.id = id
        self.username = username
        self.email = email

@login_manager.user_loader
def load_user(user_id):
    # Normally, you'd load the user from the database
    return User(user_id, 'username', 'user_email@example.com')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # This is just a simplified example
        user = User(id=1, username="user", email="user_email@example.com")
        login_user(user)
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/dashboard')
@login_required
def dashboard():
    return f'Hello, {current_user.username}! Welcome to the Dashboard.'

@app.route('/send_notification')
@login_required
def send_notification():
    # Send an email notification to the current user
    msg = Message('Notification',
                  sender='your_email@gmail.com',
                  recipients=[current_user.email])
    msg.body = 'This is a notification email.'
    mail.send(msg)
    return 'Notification sent!'

if __name__ == '__main__':
    app.run(debug=True)
