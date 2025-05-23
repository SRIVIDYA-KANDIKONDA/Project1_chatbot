from flask import Flask, render_template, request, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

# Ensure the database and predefined user exist
with app.app_context():
    db.create_all()

    # Check if "srividya" exists, if not create it
    if not User.query.filter_by(username="srividya").first():
        hashed_password = generate_password_hash("s1r2i3v4", method="pbkdf2:sha256")
        new_user = User(username="srividya", password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

@app.route('/')
def home():
    if 'username' in session:
        return render_template('chat.html', username=session['username'])
    return render_template('login.html')

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    hashed_password = generate_password_hash(data['password'], method='pbkdf2:sha256')
    new_user = User(username=data['username'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully"})

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data['username']).first()
    
    if user and check_password_hash(user.password, data['password']):
        session['username'] = user.username  # Store session
        return jsonify({"message": "Login successful", "username": user.username})
    
    return jsonify({"message": "Invalid credentials"}), 401

@app.route('/logout')
def logout():
    session.pop('username', None)
    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)