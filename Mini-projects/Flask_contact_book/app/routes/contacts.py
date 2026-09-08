from flask import Blueprint, render_template, request, redirect, url_for, flash, session

from app.extensions import db
from app.models import Contact
from app.routes.auth import login_required

contacts = Blueprint("contacts", __name__)

@contacts.route("/")
def home():
    return render_template("home.html")

@contacts.route("/add", methods=["GET"])
@login_required
def add_page():
    return render_template("add.html")

@contacts.route("/add", methods=["POST"])
@login_required
def add():
    user_id = session.get("user_id")

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

    return redirect(url_for("contacts.view_page"))

@contacts.route("/contacts")
@login_required
def view_page():
    user_id = session.get("user_id")

    contacts = Contact.query.filter_by(user_id=user_id).all()

    return render_template("contacts.html", contacts=contacts)

@contacts.route("/delete/<int:id>")
@login_required
def delete_page(id):
    user_id = session.get("user_id")
    contact = Contact.query.filter_by(
    id=id,
    user_id=user_id 
    ).first()

    if contact is None:
        return redirect(url_for("contacts.view_page"))

    db.session.delete(contact)

    db.session.commit()

    flash("Contact deleted successfully!")

    return redirect(url_for("contacts.view_page"))

@contacts.route("/edit/<int:id>")
@login_required
def edit_page(id):
    user_id = session.get("user_id")
    contact = Contact.query.filter_by(
    id=id,
    user_id=user_id
    ).first()
    if contact is None:
        return redirect(url_for("contacts.view_page"))
    return render_template("edit.html", contact=contact)

    

@contacts.route("/edit/<int:id>", methods=["POST"])
@login_required
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
        return redirect(url_for("contacts.view_page"))

    contact.name = name
    contact.phone = phone
    contact.email = email

    db.session.commit()

    flash("Contact updated successfully!")

    return redirect(url_for("contacts.view_page"))




