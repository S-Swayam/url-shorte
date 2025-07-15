# upshorte

A simple URL shortener built with Flask and SQLite.

## Features
- Shorten long URLs
- Redirect using short codes
- Tracks click counts

## Setup

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd upshorte
   ```
2. (Optional) Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the app:
   ```bash
   python app.py
   ```

## Deployment
- Make sure to set a strong `app.secret_key` in `app.py` for production.
- The database will be created automatically in the `data/` folder.
