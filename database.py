"""
Database Module for Programming Visualization Platform
Handles SQLite operations, user management, and analysis history.
"""

import sqlite3
import os
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

DATABASE_PATH = os.path.join(os.path.dirname(__file__), 'database', 'app.db')

def get_db_connection():
    """Create a database connection with row factory."""
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initialize the database with all required tables."""
    os.makedirs(os.path.dirname(DATABASE_PATH), exist_ok=True)
    conn = get_db_connection()
    cursor = conn.cursor()

    # Users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE,
            password_hash TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            theme_preference TEXT DEFAULT 'dark'
        )
    """)

    # Analysis history table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS analysis_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER DEFAULT 1,
            filename TEXT,
            language TEXT,
            code_snippet TEXT,
            analysis_result TEXT,
            visualizations TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    # Uploaded files table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS uploaded_files (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER DEFAULT 1,
            filename TEXT,
            filepath TEXT,
            language TEXT,
            file_size INTEGER,
            uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    # Reports table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER DEFAULT 1,
            analysis_id INTEGER,
            report_type TEXT,
            filepath TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (analysis_id) REFERENCES analysis_history(id)
        )
    """)

    # Create anonymous user for public access (no login required)
    try:
        conn.execute(
            "INSERT OR IGNORE INTO users (id, username, email, password_hash) VALUES (?, ?, ?, ?)",
            (1, "anonymous", "anonymous@localhost", "anonymous")
        )
    except Exception:
        pass

    conn.commit()
    conn.close()
    print("[DATABASE] Initialized successfully.")

def create_user(username, email, password):
    """Register a new user."""
    conn = get_db_connection()
    try:
        password_hash = generate_password_hash(password, method='pbkdf2:sha256', salt_length=16)
        conn.execute(
            "INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)",
            (username, email, password_hash)
        )
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def get_user_by_username(username):
    """Fetch user by username."""
    conn = get_db_connection()
    user = conn.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
    conn.close()
    return dict(user) if user else None

def get_user_by_id(user_id):
    """Fetch user by ID."""
    conn = get_db_connection()
    user = conn.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
    conn.close()
    return dict(user) if user else None

def verify_password(username, password):
    """Verify user password."""
    user = get_user_by_username(username)
    if user and check_password_hash(user['password_hash'], password):
        return user
    return None

def update_theme(user_id, theme):
    """Update user theme preference."""
    conn = get_db_connection()
    conn.execute("UPDATE users SET theme_preference = ? WHERE id = ?", (theme, user_id))
    conn.commit()
    conn.close()

def save_analysis(user_id, filename, language, code_snippet, analysis_result, visualizations):
    """Save analysis result to history."""
    conn = get_db_connection()
    import json
    try:
        result_json = json.dumps(analysis_result, default=str)
    except Exception as e:
        result_json = json.dumps({"error": f"Serialization failed: {str(e)}", "language": analysis_result.get("detected_language", "unknown")})

    try:
        viz_json = json.dumps(visualizations, default=str)
    except Exception as e:
        viz_json = json.dumps({"error": f"Visualization serialization failed: {str(e)}"})

    cursor = conn.execute(
        """INSERT INTO analysis_history 
           (user_id, filename, language, code_snippet, analysis_result, visualizations) 
           VALUES (?, ?, ?, ?, ?, ?)""",
        (user_id, filename, language, code_snippet, result_json, viz_json)
    )
    analysis_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return analysis_id

def get_user_history(user_id=None):
    """Get all analysis history for a user (or all if user_id is None)."""
    conn = get_db_connection()
    if user_id:
        rows = conn.execute(
            "SELECT * FROM analysis_history WHERE user_id = ? ORDER BY created_at DESC",
            (user_id,)
        ).fetchall()
    else:
        rows = conn.execute(
            "SELECT * FROM analysis_history ORDER BY created_at DESC"
        ).fetchall()
    conn.close()
    import json
    return [dict(row) for row in rows]

def get_analysis_by_id(analysis_id):
    """Get specific analysis by ID."""
    conn = get_db_connection()
    row = conn.execute("SELECT * FROM analysis_history WHERE id = ?", (analysis_id,)).fetchone()
    conn.close()
    if row:
        import json
        data = dict(row)
        data['analysis_result'] = json.loads(data['analysis_result'])
        data['visualizations'] = json.loads(data['visualizations'])
        return data
    return None

def save_uploaded_file(user_id, filename, filepath, language, file_size):
    """Record uploaded file."""
    conn = get_db_connection()
    conn.execute(
        "INSERT INTO uploaded_files (user_id, filename, filepath, language, file_size) VALUES (?, ?, ?, ?, ?)",
        (user_id, filename, filepath, language, file_size)
    )
    conn.commit()
    conn.close()

def get_user_files(user_id=None):
    """Get all uploaded files for a user (or all if user_id is None)."""
    conn = get_db_connection()
    if user_id:
        rows = conn.execute(
            "SELECT * FROM uploaded_files WHERE user_id = ? ORDER BY uploaded_at DESC",
            (user_id,)
        ).fetchall()
    else:
        rows = conn.execute(
            "SELECT * FROM uploaded_files ORDER BY uploaded_at DESC"
        ).fetchall()
    conn.close()
    return [dict(row) for row in rows]

def get_stats():
    """Get platform statistics."""
    conn = get_db_connection()
    stats = {}
    stats['total_users'] = conn.execute("SELECT COUNT(*) FROM users").fetchone()[0]
    stats['total_analyses'] = conn.execute("SELECT COUNT(*) FROM analysis_history").fetchone()[0]
    stats['total_files'] = conn.execute("SELECT COUNT(*) FROM uploaded_files").fetchone()[0]

    lang_stats = conn.execute(
        "SELECT language, COUNT(*) as count FROM analysis_history GROUP BY language"
    ).fetchall()
    stats['language_stats'] = {row['language']: row['count'] for row in lang_stats}
    conn.close()
    return stats

def save_report(user_id, analysis_id, report_type, filepath):
    """Save generated report."""
    conn = get_db_connection()
    conn.execute(
        "INSERT INTO reports (user_id, analysis_id, report_type, filepath) VALUES (?, ?, ?, ?)",
        (user_id, analysis_id, report_type, filepath)
    )
    conn.commit()
    conn.close()

def get_user_reports(user_id=None):
    """Get all reports for a user (or all if user_id is None)."""
    conn = get_db_connection()
    if user_id:
        rows = conn.execute(
            "SELECT * FROM reports WHERE user_id = ? ORDER BY created_at DESC",
            (user_id,)
        ).fetchall()
    else:
        rows = conn.execute(
            "SELECT * FROM reports ORDER BY created_at DESC"
        ).fetchall()
    conn.close()
    return [dict(row) for row in rows]
