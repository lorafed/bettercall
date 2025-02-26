from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_required, current_user

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fundraising.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)
login_manager = LoginManager(app)

# Define roles
ROLES = {'admin': 1, 'fundraiser': 2, 'manager': 3}

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    role = db.Column(db.Integer, nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/admin/users')
@login_required
def manage_users():
    if current_user.role != ROLES['admin']:
        return redirect(url_for('dashboard'))
    
    users = User.query.all()
    return render_template('manage_users.html', users=users, roles=ROLES)

@app.route('/admin/users/<int:user_id>', methods=['GET', 'POST'])
@login_required
def edit_user(user_id):
    if current_user.role != ROLES['admin']:
        return redirect(url_for('dashboard'))

    user = User.query.get(user_id)
    if request.method == 'POST':
        user.role = int(request.form['role'])
        db.session.commit()
        return redirect(url_for('manage_users'))

    return render_template('edit_user.html', user=user, roles=ROLES)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
