from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///contacts.db"

db = SQLAlchemy(app)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)


@app.route("/contacts", methods=["GET"])
def get_contacts():
    contacts = Contact.query.all()

    return {
        "contacts": [
            {
                "id": contact.id,
                "name": contact.name,
                "phone": contact.phone
            }
            for contact in contacts
        ]
    }

@app.route("/contacts", methods=["POST"])
def create_contact():
    data = request.get_json()

    new_contact = Contact(
        name=data["name"],
        phone=data["phone"]
    )

    db.session.add(new_contact)
    db.session.commit()

    return {
        "message": "Contact created successfully",
        "contact": {
            "id": new_contact.id,
            "name": new_contact.name,
            "phone": new_contact.phone
        }
    }, 201

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)





