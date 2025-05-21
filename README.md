# Project1_chatbot
# 🔐 Secured Chat App

A simple and stylish web-based chat application built with Flask that features user authentication and real-time messaging.

## 🚀 Features

- User Registration and Login
- Passwords hashed using `pbkdf2:sha256`
- Session-based authentication
- Real-time chat interface (template set up for Socket.IO)
- Aesthetic UI with animated gradient background

## 🛠️ Tech Stack

- Python (Flask)
- SQLite
- HTML/CSS/JavaScript
- Jinja2 for templating
- Bootstrap-inspired styling
- Socket.IO (front-end script loaded)

## 📁 File Structure

- `app.py` – Flask backend and routes
- `templates/`
  - `login.html` – Login form
  - `chat.html` – Chat interface
- `static/styles.css` – UI styling
- `users.db` – SQLite database for user credentials

## ▶️ Getting Started

1. **Install dependencies**:
   ```bash
   pip install flask flask_sqlalchemy werkzeug
