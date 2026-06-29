"""
Authentication Module for Programming Visualization Platform
Handles user registration, login, logout, and session management.
"""

from functools import wraps
from flask import session, redirect, url_for, flash
from database import verify_password, create_user, get_user_by_id

def login_required(f):
    """Decorator to require login for routes."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in to access this page.', 'warning')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

def admin_required(f):
    """Decorator to require admin privileges."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in to access this page.', 'warning')
            return redirect(url_for('login'))
        user = get_user_by_id(session['user_id'])
        if not user or user.get('username') != 'admin':
            flash('Admin access required.', 'danger')
            return redirect(url_for('dashboard'))
        return f(*args, **kwargs)
    return decorated_function

def login_user(username, password):
    """Authenticate and log in a user."""
    user = verify_password(username, password)
    if user:
        session['user_id'] = user['id']
        session['username'] = user['username']
        session['theme'] = user.get('theme_preference', 'dark')
        return True
    return False

def logout_user():
    """Log out the current user."""
    session.clear()

def register_user(username, email, password):
    """Register a new user."""
    if len(password) < 6:
        return False, "Password must be at least 6 characters long."
    if len(username) < 3:
        return False, "Username must be at least 3 characters long."
    if create_user(username, email, password):
        return True, "Registration successful! Please log in."
    return False, "Username or email already exists."

def get_current_user():
    """Get the currently logged in user."""
    if 'user_id' in session:
        return get_user_by_id(session['user_id'])
    return None
