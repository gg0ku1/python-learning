from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    session
)

from extensions import db

from models import Contact, User

from werkzeug.security import generate_password_hash, check_password_hash

from sqlalchemy.exc import IntegrityError

from flask_migrate import Migrate


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///contacts.db"

db.init_app(app)
migrate = Migrate(app, db)
app.secret_key = "supersecretkey"


@app.route("/register", methods=["GET", "POST"])
def register_page():

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

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
            return redirect(url_for("register_page"))

        return redirect(url_for("register_page"))
        
    return render_template("register.html")



@app.route("/login", methods=["GET", "POST"])
def login_page():

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            session["user_id"] = user.id
            return redirect(url_for("view_page"))

    

    return render_template("login.html")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/add", methods=["GET"])
def add_page():
    user_id = session.get("user_id")

    if user_id is None:
        return redirect(url_for("login_page"))

    return render_template("add.html")

@app.route("/add", methods=["POST"])
def add():
    user_id = session.get("user_id")

    if user_id is None:
        return redirect(url_for("login_page"))
    name = request.form["name"]
    phone = request.form["phone"]
    email = request.form["email"]
    name = name.strip()
    phone = phone.strip()
    email = email.strip()

    if not name or not phone or not email:
        return("invalid input, please fill all fields correctly")

    new_contact = Contact(
    name=name,
    phone=phone,
    email=email,
    user_id=user_id)

    db.session.add(new_contact)
    db.session.commit()

    flash("Contact added successfully!")

    return redirect(url_for("view_page"))

@app.route("/logout", methods=["GET"])
def logout():
    session.pop("user_id", None)

    return redirect(url_for("login_page"))

@app.route("/contacts")
def view_page():
    user_id = session.get("user_id")

    if user_id is None:
        return redirect(url_for("login_page"))

    contacts = Contact.query.filter_by(user_id=user_id).all()

    return render_template("contacts.html", contacts=contacts)

@app.route("/delete/<int:id>")
def delete_page(id):
    user_id = session.get("user_id")
    contact = Contact.query.filter_by(
    id=id,
    user_id=user_id 
    ).first()

    if contact is None:
        return redirect(url_for("view_page"))

    db.session.delete(contact)

    db.session.commit()

    flash("Contact deleted successfully!")

    return redirect(url_for("view_page"))

@app.route("/edit/<int:id>")
def edit_page(id):
    user_id = session.get("user_id")
    contact = Contact.query.filter_by(
    id=id,
    user_id=user_id
    ).first()
    if contact is None:
            return redirect(url_for("view_page"))
    return render_template("edit.html", contact=contact)

    

@app.route("/edit/<int:id>", methods=["POST"])

def edit(id):
    name = request.form["name"]
    phone = request.form["phone"]
    email = request.form["email"]
    name = name.strip()
    phone = phone.strip()
    email = email.strip()

    if not name or not phone or not email:
        return("no input")

    user_id = session.get("user_id")
    contact = Contact.query.filter_by(
    id=id,
    user_id=user_id
    ).first()
    if contact is None:
            return redirect(url_for("view_page"))

    contact.name = name
    contact.phone = phone
    contact.email = email

    db.session.commit()

    flash("Contact updated successfully!")

    return redirect(url_for("view_page"))






if __name__ == "__main__":
    app.run(debug=True)


