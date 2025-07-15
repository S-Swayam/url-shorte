from flask import Flask, request, redirect, render_template, url_for, flash
import string
import random
import os
from database import init_db, save_url, get_url, click_count, get_short_code

# Create the Flask app
app = Flask(__name__)
# Secret key for session and flash messages
app.secret_key = 'b2e7f8c1-4a3d-4e2b-9c6a-7f1e2d3c4b5a'  # Use a strong random value in production

# Initialize the database and table
init_db()

# Function to generate a random short code
def generate_short_code(length=6):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=length))

# Check if a short code is already used
def is_code_taken(short_code):
    return get_url(short_code) is not None

# Home page: form to submit URL and show result
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        original_url = request.form.get('original_url')
        if not original_url:
            flash('Please enter a URL.')
            return render_template('index.html')
        # Check if this URL was already shortened
        short_code = get_short_code(original_url)
        if not short_code:
            # Generate a unique short code
            while True:
                short_code = generate_short_code()
                if not is_code_taken(short_code):
                    break
            save_url(short_code, original_url)
        short_url = request.host_url + short_code
        return render_template('index.html', short_url=short_url)
    return render_template('index.html')

# Redirect from short code to original URL
@app.route('/<short_code>')
def redirect_short_url(short_code):
    url = get_url(short_code)
    if url:
        click_count(short_code)
        return redirect(url)
    flash('Invalid short URL.')
    return redirect(url_for('index'))

# Run the app
if __name__ == '__main__':
    app.run(debug=True)

