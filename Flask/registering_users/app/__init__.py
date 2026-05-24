import functools
from flask import (
    Flask,
    session,
    render_template,
    request,
    abort,
    flash,
    redirect,
    url_for,    
)
from passlib.hash import pbkdf2_sha256

app = Flask(__name__)
# Secret key generated with secrets.token_urlsafe()
app.secret_key = "lkaQT-kAb6aIvqWETVcCQ28F-j-rP_PSEaCDdTynkXA"

users = {
    'admin@gmail.com': pbkdf2_sha256.hash('123456')
}

def login_required(route):
    @functools.wraps(route)
    def route_wrapper(*args, **kwargs):
        email = session.get("email")
        if not email or email not in users:
            return redirect( url_for("login") )
        return route(*args, **kwargs)
    return route_wrapper

@app.get("/")
@login_required
def home():
    return render_template("home.html", email=session.get("email") in users)

@app.get("/protected")
@login_required # Decorator: Bọc function
def protected():
    if not session.get("email"):
        abort(401)
    return render_template("protected.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    email = ""
    
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        stored_password = users.get(email)
        
        if not email or not password:
            return "Vui lòng nhập đầy đủ thông tin"
                
        if stored_password and pbkdf2_sha256.verify(password, users.get(email)):
            session["email"] = email
            return redirect(url_for("protected"))
        
        flash("Incorrect e-mail or password.")
    
    return render_template("login.html", email=email)

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        email = request.form.get("email")
        password = pbkdf2_sha256.hash(request.form.get("password"))
    
        # Store account to `users`
        users[email] = password
        # session["email"] = email
        
        print(users)
        flash("Successfully signed up.")
        return redirect(url_for("login"))
        
    return render_template("signup.html")