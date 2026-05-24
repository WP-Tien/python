import re
from flask import Flask, render_template, url_for, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user, logout_user # Quản lý đăng nhập user/session.
from sqlalchemy import text
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash
from urllib.parse import urlparse
from datetime import timedelta

db = SQLAlchemy()
login_manager = LoginManager()

class User(UserMixin, db.Model):
    id = db.Column( db.Integer, primary_key=True )
    username = db.Column( db.String(80), unique=True, nullable=False )
    email = db.Column( db.String(120), unique=True, nullable=False )
    password_hash = db.Column( db.String(255), nullable=False )
    
    def __repr__(self):
        return f"<User {self.username}>"    

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'dev-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['REMEMBER_COOKIE_DURATION'] = timedelta(days=15)

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "login"

    @app.route("/health/db")
    def health_db():
        try:
            db.session.execute(text("SELECT 1"))
            return {"db": "ok"}, 200
        except Exception as e:
            return {"db": "error", "detail": str(e)}, 500

    with app.app_context():
        db.create_all()

    def _is_safe_local_path(target: str) -> bool:
        if not target:
            return False;
        parts = urlparse(target)
        return parts.scheme == "" and parts.netloc == "" and target.startswith("/")

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/dashboard")
    @login_required
    def dashboard():
        return render_template("dashboard.html")
    
    @app.route("/test")
    @login_required
    def test():
        return "test route"

    @app.route("/logout")
    def logout():
        logout_user()
        flash("You have been logged out", "success")
        return redirect(url_for("index"))
    
    @app.route("/change-password", methods=["GET", "POST"])
    @login_required
    def change_password():
        errors = []
        
        if request.method == "POST":
            current_pw = request.form.get("current_password") or ""
            new_pw = request.form.get("new_password") or ""
            confirm_pw = request.form.get("confirm_password") or ""
            
            if not check_password_hash(current_user.password_hash, current_pw):
                errors.append("Current password is incorrect")
                
            if len(new_pw) < 6:
                errors.append("New passwords need to be at least 6 characters")
                
            if new_pw != confirm_pw:
                errors.append("New passwords and confirmation do not match")
                
            if not errors:
                current_user.password_hash = generate_password_hash(new_pw)
                db.session.commit()
                
                flash("Your password has been updated", "success")
                return redirect(url_for("dashboard"))
            
        return render_template("change_password.html", errors=errors)
            
    @app.route("/register", methods=["GET", "POST"])
    def register():
        errors = []
        if request.method == "POST":
            username = (request.form.get("username") or "").strip()
            email = (request.form.get("email") or "").strip()
            password = request.form.get("password") or ""
            confirm = request.form.get("confirm_password") or ""
            
            if not(3 <= len(username) <= 80):
                errors.append("Username must be between 3 and 80 character")
            if not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email):
                errors.append("Please enter a valid email address")
            if len(password) < 6:
                errors.append("Password needs to be at least 6 characters")
            if password != confirm:
                errors.append("Password dont't match")        
            if not errors:
                
                try:
                    pw_hash = generate_password_hash(password)
                    user = User(username=username, email=email, password_hash=pw_hash)
                    db.session.add(user)
                    db.session.commit()
                    
                    flash("Account created successfully!, Please login", "success")
                    return redirect(url_for('login'))
                    
                except IntegrityError:
                    db.session.rollback()
                    errors.append("That username or email is already registered")
                    
                # return f"Valid input received - {email}"
            
            # print("Form submitted", username, email, password, confirm)
            
            # return f"Received data - {email}"
        
        return render_template("register.html", errors=errors)

    @app.route("/login", methods=["POST", "GET"])
    def login():
        errors = []
        user = ''
        
        if request.method == "POST":
            email = (request.form.get("email") or "").strip()
            password = request.form.get("password") or ""
            
            if not email:
                errors.append("Email is required")
                
            if not password:
                errors.append("Password is required")
                
            if not errors:
                user = User.query.filter_by(email=email).first()
                
            if not user or not check_password_hash(user.password_hash, password):
                errors.append("Invalid email or password")
            else:
                remember_flag = request.form.get("remember") == "1"
                
                login_user(user, remember=remember_flag)
                
                flash(f"Welcome back {user.username}", "success")
                
                # urlparse("https://example/com/page")
                # scheme='https', netloc='example.com', path='/page'
                
                remember_flag = request.form.get("remember") == "1"
                
                next_url = request.form.get("next") or request.args.get("next") or ""
                
                if _is_safe_local_path(next_url):
                    return redirect(next_url)
                
                return redirect(url_for("dashboard"))
        
        return render_template("login.html", errors=errors)
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=5555)