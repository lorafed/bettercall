from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
import os
import sqlite3

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'backups/'

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/admin/backup', methods=['GET'])
def backup_database():
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    conn = sqlite3.connect('fundraising.db')
    backup_file = os.path.join(app.config['UPLOAD_FOLDER'], 'backup.db')
    with open(backup_file, 'w') as f:
        for line in conn.iterdump():
            f.write('%s\n' % line)
    conn.close()
    return 'Database backup created successfully!'

@app.route('/admin/restore', methods=['POST'])
def restore_database():
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        conn = sqlite3.connect('fundraising.db')
        with open(filepath, 'r') as f:
            conn.executescript(f.read())
        conn.close()
        return 'Database restored successfully!'
    return 'Failed to restore database.'

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'db'}

if __name__ == '__main__':
    app.run(debug=True)
