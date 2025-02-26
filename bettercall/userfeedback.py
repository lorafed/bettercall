from flask import Flask, request, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fundraising.db'
db = SQLAlchemy(app)

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    feedback = db.Column(db.String(500))

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        user_feedback = request.form['feedback']
        new_feedback = Feedback(user_id=1, feedback=user_feedback)  # Assume user_id is 1 for this example
        db.session.add(new_feedback)
        db.session.commit()
        return redirect(url_for('thank_you'))
    return render_template('feedback.html')

@app.route('/thank_you')
def thank_you():
    return 'Thank you for your feedback!'

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
