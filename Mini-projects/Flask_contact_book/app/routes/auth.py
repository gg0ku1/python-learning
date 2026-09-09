from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.exc import IntegrityError
from functools import wraps

from app.extensions import db
from app.models import User

auth = Blueprint("auth", __name__)

def login_required(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        user_id = session.get("user_id")

        if user_id is None:
            return redirect(url_for("auth.login_page"))

        return func(*args, **kwargs)

    return wrapper

@auth.route("/register", methods=["GET", "POST"])
def register_page():

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        username = username.strip()
        if not username or not password:
            flash("Username and password are required.")
            return redirect(url_for("auth.register_page"))
        hashed_password = generate_password_hash(password)

        new_user = User(
            username = username,
            password = hashed_password
        )

        db.session.add(new_user)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            flash("Username already exists!")
            return redirect(url_for("auth.register_page"))

        flash("Registration successful! Please log in.")
        return redirect(url_for("auth.login_page"))
        
    return render_template("register.html")



@auth.route("/login", methods=["GET", "POST"])
def login_page():

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        username = username.strip()

        if not username or not password:
            flash("Username and password are required.")
            return redirect(url_for("auth.login_page"))

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            session["user_id"] = user.id
            return redirect(url_for("contacts.view_page"))
        
        flash("Invalid username or password.")
        return redirect(url_for("auth.login_page"))

    
    
    return render_template("login.html")

@auth.route("/logout", methods=["GET"])
def logout():
    session.pop("user_id", None)

    return redirect(url_for("auth.login_page"))