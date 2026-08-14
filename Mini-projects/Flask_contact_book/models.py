from extensions import db

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    email = db.Column(db.String(100))

new_contact = Contact(
    name=name,
    phone=phone,
    email=email
)

db.session.add(new_contact)
db.session.commit()