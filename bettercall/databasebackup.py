import sqlite3
import shutil
import os

DATABASE = 'fundraising.db'
BACKUP = 'backup_fundraising.db'

def backup_database():
    if os.path.exists(DATABASE):
        shutil.copy(DATABASE, BACKUP)
        print(f'Backup of {DATABASE} created as {BACKUP}')
    else:
        print(f'Database {DATABASE} does not exist.')

def restore_database():
    if os.path.exists(BACKUP):
        shutil.copy(BACKUP, DATABASE)
        print(f'Restored {DATABASE} from {BACKUP}')
    else:
        print(f'Backup {BACKUP} does not exist.')

# Example usage
backup_database()
restore_database()
