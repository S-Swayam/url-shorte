import sqlite3
import os

# Path to the SQLite database file
DB_PATH = 'data/database.db'

# Create the data folder and table if they don't exist
def init_db():
    os.makedirs('data', exist_ok=True)
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS urls (
                short_code TEXT PRIMARY KEY,
                original_url TEXT NOT NULL,
                clicks INTEGER DEFAULT 0
            )
        ''')

# Get the short code for a given original URL (if it exists)
def get_short_code(original_url):
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.execute('SELECT short_code FROM urls WHERE original_url = ?', (original_url,))
        row = cur.fetchone()
        return row[0] if row else None

# Save a new short code and original URL
def save_url(short_code, original_url):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute('INSERT OR IGNORE INTO urls (short_code, original_url) VALUES (?, ?)', (short_code, original_url))

# Get the original URL for a given short code
def get_url(short_code):
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.execute('SELECT original_url FROM urls WHERE short_code = ?', (short_code,))
        row = cur.fetchone()
        return row[0] if row else None

# Increment the click count for a short code
def click_count(short_code):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute('UPDATE urls SET clicks = clicks + 1 WHERE short_code = ?', (short_code))

