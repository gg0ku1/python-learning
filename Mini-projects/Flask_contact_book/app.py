from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash
)

from extensions import db

from models import Contact

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///contacts.db"

db.init_app(app)
app.secret_key = "supersecretkey"

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/add", methods=["GET"])
def add_page():
    return render_template("add.html")

@app.route("/add", methods=["POST"])
def add():
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
    email=email)

    db.session.add(new_contact)
    db.session.commit()

    flash("Contact added successfully!")

    return redirect(url_for("view_page"))

@app.route("/contacts")
def view_page():
    contacts = Contact.query.all()
    return render_template("contacts.html", contacts=contacts)

@app.route("/delete/<int:id>")
def delete_page(id):
    contact = db.session.get(Contact, id)

    db.session.delete(contact)

    db.session.commit()
    
    flash("Contact deleted successfully!")

    return redirect(url_for("view_page"))

@app.route("/edit/<int:id>")
def edit_page(id):
    contact = db.session.get(Contact, id)
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

    contact = db.session.get(Contact, id)

    contact.name = name
    contact.phone = phone
    contact.email = email

    db.session.commit()

    flash("Contact updated successfully!")

    return redirect(url_for("view_page"))





if __name__ == "__main__":
    app.run(debug=True)


