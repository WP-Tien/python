import logging
from flask import flash, Blueprint, request, render_template, redirect
from flask_login import LoginManager, login_user, login_required, current_user

from sqlalchemy import text 
from werkzeug.security import generate_password_hash, check_password_hash

from app.extensions import db
from app.models import User
from app.forms import LoginForm, RegisterForm

main = Blueprint("main", __name__)

# ROUTES
@main.route("/health/db")
def health_db():
    """Check database connection

    Returns:
        dict: status and message with code
    """
    try:
        db.session.execute(text("SELECT 1"))
        
        return {
            "status": "success",
            "message": "Database connected"
        }, 200
    
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }, 500        

@main.route("/", methods = ['GET', 'POST'])
def start():
    return redirect("/home")

@main.route("/home", methods = ["GET", "POST"])
@login_required
def home():
    return render_template('home.html', name=current_user.username)

@main.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
        
    # Checks if the incoming request is a valid form submission
    if form.validate_on_submit():
        try:
            user = (form.username.data or "").strip()
            password = (form.password.data or "").strip()
            
            if user:
                get_user = User.query.filter_by(username=user).first()
                                                
                if get_user and check_password_hash(get_user.password, password):
                    remember_flag = form.remember.data

                    login_user(get_user, remember=remember_flag)
                    
                    flash(f"Welcome back {get_user.username}", "success")

                    return redirect(url_for("main.home"))
                else:
                    flash("Invalid email or password", "danger")
                                
        except Exception as e:
            logging.critical(
                "The following error occurred when logging in: {}".format(str(e))
            )
            
            flash("Something went wrong", "danger")
            
    return render_template(
        "signin.html",
        form=form
    )
    
@main.route("/signup", methods=["GET", "POST"])
def signup():
    form = RegisterForm()
    
    if form.validate_on_submit():
        email = (form.email.data or "").strip()
        user = (form.username.data or "").strip()
        password = form.password.data or ""
        confirm = form.confirm.data or ""
    
        try:
            hashed_password = generate_password_hash(password, method="pbkdf2:sha256")
            create_user = User(username=user, email=email, password=hashed_password)
            db.session.add(create_user)
            db.session.commit()
            
            flash("Account created successfully!, Please login", "success")
            return redirect(url_for('main.login'))
    
        except InterruptedError:
            db.session.rollback()
            flash("That username or email is already registered", "danger")
        
    return render_template("signup.html", form=form)