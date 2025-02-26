import csv
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
import sqlite3

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'csv'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def import_csv_to_db(filepath):
    conn = sqlite3.connect('fundraising.db')
    cursor = conn.cursor()
    with open(filepath, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cursor.execute(
                "INSERT INTO donors (name, phone, timezone, history) VALUES (?, ?, ?, ?)",
                (row['name'], row['phone'], row['timezone'], row['history'])
            )
    conn.commit()
    conn.close()

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            import_csv_to_db(filepath)
            return redirect(url_for('upload_file'))
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
