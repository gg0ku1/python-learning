from flask import Flask, render_template, request, redirect, url_for, json

from database import (
    create_database,
    add_contact,
    get_contacts,
    delete_contact,
    get_contact,
    update_contact
)

app = Flask(__name__)


create_database()


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

    add_contact(name, phone, email)
    return redirect(url_for("home"))

@app.route("/contacts")
def view_page():
    return render_template("contacts.html", contacts = get_contacts())

@app.route("/delete/<int:id>")
def delete_page(id):
    delete_contact(id)

    return redirect(url_for("view_page"))

@app.route("/edit/<int:id>")
def edit_page(id):
    contact = get_contact(id)
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

    update_contact(id,name, phone, email)
    return redirect(url_for("view_page"))





if __name__ == "__main__":
    app.run(debug=True)

#sick and tired pls overlook one time