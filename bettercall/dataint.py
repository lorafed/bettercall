import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('fundraising.db')
cursor = conn.cursor()

# Create tables for donors, call logs, and messages
cursor.execute('''
CREATE TABLE IF NOT EXISTS donors (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    phone TEXT NOT NULL,
    timezone TEXT,
    history TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS call_logs (
    id INTEGER PRIMARY KEY,
    donor_id INTEGER,
    call_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    outcome TEXT,
    FOREIGN KEY(donor_id) REFERENCES donors(id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS follow_up_messages (
    id INTEGER PRIMARY KEY,
    donor_id INTEGER,
    message TEXT,
    send_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(donor_id) REFERENCES donors(id)
)
''')

# Example function to add a donor
def add_donor(name, phone, timezone, history):
    cursor.execute('INSERT INTO donors (name, phone, timezone, history) VALUES (?, ?, ?, ?)', 
                   (name, phone, timezone, history))
    conn.commit()

# Example function to log a call
def log_call(donor_id, outcome):
    cursor.execute('INSERT INTO call_logs (donor_id, outcome) VALUES (?, ?)', 
                   (donor_id, outcome))
    conn.commit()

# Example function to add a follow-up message
def add_follow_up_message(donor_id, message):
    cursor.execute('INSERT INTO follow_up_messages (donor_id, message) VALUES (?, ?)', 
                   (donor_id, message))
    conn.commit()

# Example usage
add_donor('John Doe', '+1234567890', 'PST', 'High School Program')
log_call(1, 'Successful Donation')
add_follow_up_message(1, 'Thank you for your generous donation!')

# Close the connection when done
conn.close()
