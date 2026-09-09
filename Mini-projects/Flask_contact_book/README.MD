# 📇 Flask Contact Book

A full-stack learning project built while progressing from basic Python CLI applications into Flask, databases, authentication, and proper application structure.

This project started as a simple command-line Contact Book that stored contacts in JSON. It was later rebuilt as a Flask web application using SQLite and SQLAlchemy, with user authentication and per-user contact management.

The main purpose of this project was **learning**, not building a production-ready contact management system.

---

## 📌 Project Goal

The original goal was simple:

> Build a Contact Book that allows users to store, edit, view, and delete contacts.

However, the project became an opportunity to learn how a real Flask application is structured.

During the project I learned and implemented:

- Flask
- Routing
- HTTP GET and POST
- Jinja2 templates
- HTML forms
- Form validation
- Redirects
- `url_for()`
- Flash messages
- Sessions
- Authentication
- Password hashing
- Decorators
- Blueprints
- Application factories
- SQLAlchemy
- SQLite
- Database relationships
- Foreign keys
- Flask-Migrate
- Database migrations
- Error handlers
- Application structure
- Refactoring
- DRY principles
- Basic security concepts

---

# 🧱 Project Evolution

This project was not built from scratch as a complex Flask application.

It evolved through several stages.

## Stage 1 — CLI Contact Book

The first version was a command-line Python application.

It used a JSON file to persist contacts.

The basic idea was:

```text
Program
   ↓
Read JSON file
   ↓
Load contacts
   ↓
Perform CRUD operation
   ↓
Write JSON file
```

This version helped reinforce:

- Dictionaries
- Lists
- Functions
- File handling
- JSON
- CRUD logic
- Exception handling

Example JSON structure:

```json
[
    {
        "name": "John",
        "phone": "1234567890",
        "email": "john@example.com"
    }
]
```

The CLI version worked, but it was limited by the fact that all data was stored in a JSON file.

---

# 🌐 Stage 2 — Converting the Project to Flask

The next step was turning the CLI application into a web application.

Instead of:

```text
User
 ↓
Terminal
 ↓
Python program
```

the application became:

```text
Browser
 ↓
HTTP Request
 ↓
Flask Route
 ↓
Python Logic
 ↓
Database
 ↓
HTTP Response
 ↓
HTML Template
 ↓
Browser
```

This introduced the basic web development request/response cycle.

---

# 🐍 Flask Basics

## Routes

Flask routes connect URLs to Python functions.

Example:

```python
@contacts.route("/contacts")
@login_required
def view_page():
    ...
```

The route tells Flask:

> When a request is made to `/contacts`, run this function.

I learned that a route can also specify which HTTP methods it accepts.

For example:

```python
@contacts.route("/add", methods=["GET"])
```

and:

```python
@contacts.route("/add", methods=["POST"])
```

These represent two different purposes.

### GET

Used to display the form.

```text
GET /add
    ↓
Display add contact form
```

### POST

Used to submit the form.

```text
POST /add
    ↓
Read submitted data
    ↓
Validate it
    ↓
Create contact
    ↓
Save to database
```

---

# 📝 HTML Forms

Flask receives submitted form data through:

```python
request.form
```

For example:

```python
name = request.form["name"]
phone = request.form["phone"]
email = request.form["email"]
```

I learned that the browser sends the form data to the Flask route, and Flask makes that data available through `request.form`.

---

# 🔀 Redirects

After performing an action, the application redirects the user rather than rendering the next page directly.

For example:

```python
return redirect(url_for("contacts.view_page"))
```

This is useful after operations such as:

- Adding a contact
- Editing a contact
- Logging in
- Registering
- Logging out

This helped me understand the difference between:

```python
render_template()
```

and:

```python
redirect()
```

`render_template()` renders an HTML page.

`redirect()` tells the browser to make another request to a different route.

---

# 🔗 `url_for()`

Instead of hardcoding URLs:

```html
<a href="/contacts">
```

the application uses:

```jinja2
<a href="{{ url_for('contacts.view_page') }}">
```

This becomes particularly important after introducing Blueprints.

---

# 🎨 Jinja Templates

The project uses Jinja templates to generate dynamic HTML.

Templates inherit from a common layout:

```jinja2
{% extends "base.html" %}
```

and insert page-specific content:

```jinja2
{% block content %}
...
{% endblock %}
```

This avoids duplicating the entire HTML structure across every page.

---

# 🧩 Template Inheritance

The main layout is stored in:

```text
templates/base.html
```

Individual pages extend it.

For example:

```text
base.html
    ↓
home.html

base.html
    ↓
login.html

base.html
    ↓
register.html

base.html
    ↓
contacts.html

base.html
    ↓
add.html

base.html
    ↓
edit.html
```

This was an important introduction to reusable templates.

---

# 💬 Flash Messages

The application uses Flask's flash messaging system to display feedback to users.

Example:

```python
flash("Contact added successfully!")
```

The base template retrieves the messages:

```jinja2
{% with messages = get_flashed_messages() %}
    {% if messages %}
        {% for message in messages %}
            <div class="alert alert-success">
                {{ message }}
            </div>
        {% endfor %}
    {% endif %}
{% endwith %}
```

Flash messages are used for things such as:

- Successful registration
- Successful contact creation
- Successful contact update
- Failed login
- Missing form fields
- Duplicate usernames

---

# 🗄️ Database

The project eventually moved away from JSON storage and uses:

```text
SQLite
```

with:

```text
SQLAlchemy
```

SQLite is the actual database.

SQLAlchemy is the ORM used to interact with the database using Python objects rather than writing SQL for every operation.

---

# 🧠 SQLAlchemy Models

The application has two main models:

```python
class User(db.Model):
    ...
```

and:

```python
class Contact(db.Model):
    ...
```

The database structure is essentially:

```text
User
 ├── id
 ├── username
 └── password

Contact
 ├── id
 ├── name
 ├── phone
 ├── email
 └── user_id
```

---

# 🔑 Primary Keys

Each table has an ID.

For example:

```python
id = db.Column(db.Integer, primary_key=True)
```

The primary key uniquely identifies a row.

For contacts:

```text
1 → John
2 → Sarah
3 → Alex
```

---

# 🔗 Foreign Keys

Each contact contains:

```python
user_id = db.Column(
    db.Integer,
    db.ForeignKey("user.id"),
)
```

This connects a contact to the user who owns it.

The relationship is:

```text
User
 │
 ├── Contact
 ├── Contact
 └── Contact
```

This means multiple contacts can belong to one user.

---

# 🔄 SQLAlchemy Relationship

The `User` model contains:

```python
contacts = db.relationship("Contact", backref="user")
```

This represents the relationship between users and contacts.

It is a:

```text
One User → Many Contacts
```

relationship.

---

# 🔐 Authentication

The application includes:

- Registration
- Login
- Logout
- Password hashing
- Session-based authentication

The authentication flow is:

```text
Register
   ↓
Create User
   ↓
Hash Password
   ↓
Save User
```

Then:

```text
Login
   ↓
Find User
   ↓
Check Password
   ↓
Store user_id in Session
   ↓
User is authenticated
```

---

# 🔒 Password Hashing

Passwords are never stored as plain text.

The application uses Werkzeug:

```python
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
```

During registration:

```python
hashed_password = generate_password_hash(password)
```

The hash is stored instead of the original password.

During login:

```python
check_password_hash(user.password, password)
```

checks whether the entered password matches the stored hash.

This was an important security concept:

> Passwords should not be stored directly in a database.

---

# 🍪 Sessions

After successful login:

```python
session["user_id"] = user.id
```

The application can then determine which user is logged in.

For example:

```python
user_id = session.get("user_id")
```

The session is also used by the application to determine which UI elements should be displayed.

For example:

```jinja2
{% if session.get("user_id") %}
```

can be used to determine whether the user is logged in.

---

# 🛡️ `login_required` Decorator

One of the more important concepts learned during this project was decorators.

A custom decorator was created:

```python
def login_required(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        user_id = session.get("user_id")

        if user_id is None:
            return redirect(url_for("auth.login_page"))

        return func(*args, **kwargs)

    return wrapper
```

It can then be used like:

```python
@contacts.route("/contacts")
@login_required
def view_page():
    ...
```

This means the route can only be accessed by an authenticated user.

---

# 🧠 What I Learned About Decorators

The decorator helped reinforce several Python concepts.

A function can be passed into another function:

```python
def decorator(func):
    ...
```

A wrapper function can be created:

```python
def wrapper(*args, **kwargs):
    ...
```

The decorator returns that wrapper:

```python
return wrapper
```

And:

```python
@login_required
def view_page():
    ...
```

is essentially shorthand for applying the decorator to the function.

---

# `@wraps`

The decorator uses:

```python
from functools import wraps
```

and:

```python
@wraps(func)
```

This preserves important metadata from the original function.

It is good practice when writing decorators.

---

# 👤 User Ownership

Authentication alone isn't enough.

A logged-in user should only be able to access **their own contacts**.

Therefore queries use both:

```python
id=id,
user_id=user_id
```

For example:

```python
contact = Contact.query.filter_by(
    id=id,
    user_id=user_id
).first()
```

This is important.

Simply checking:

```python
id=id
```

would allow a logged-in user to potentially access another user's contact if they knew its ID.

The application therefore uses both:

```text
Authentication
+
Authorization / Ownership
```

Authentication asks:

> Who are you?

Authorization asks:

> Are you allowed to access this resource?

This distinction was an important lesson from the project.

---

# 🧱 Blueprints

The application initially had routes in one file.

As the application became larger, the routes were separated into Blueprints.

Current structure:

```text
app/
├── __init__.py
├── extensions.py
├── models.py
└── routes/
    ├── __init__.py
    ├── auth.py
    └── contacts.py
```

Authentication routes are in:

```text
routes/auth.py
```

Contact-related routes are in:

```text
routes/contacts.py
```

---

# 🧩 Why Blueprints?

Instead of putting everything into one huge file:

```text
app.py
    ├── login
    ├── register
    ├── logout
    ├── add
    ├── edit
    ├── delete
    └── contacts
```

the application separates responsibilities.

```text
auth.py
    ├── register
    ├── login
    └── logout

contacts.py
    ├── home
    ├── add
    ├── edit
    ├── delete
    └── view
```

This makes the application easier to understand and maintain.

---

# 🏭 Application Factory

The application uses:

```python
def create_app():
```

instead of creating the Flask application globally in one file.

The factory creates and configures the application.

It handles:

- Flask initialization
- Configuration
- Database initialization
- Migration initialization
- Blueprint registration
- Error handlers

The application is then created in:

```text
run.py
```

with:

```python
from app import create_app

app = create_app()

app.run(debug=True)
```

---

# 🔌 Extensions

Database initialization was separated into:

```text
app/extensions.py
```

containing:

```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
```

The database is then connected to the Flask application with:

```python
db.init_app(app)
```

This separation is useful because the extension itself is created independently of the application.

---

# 📁 Final Project Structure

The final structure is:

```text
Flask_contact_book/
│
├── app/
│   ├── __init__.py
│   ├── extensions.py
│   ├── models.py
│   │
│   └── routes/
│       ├── __init__.py
│       ├── auth.py
│       └── contacts.py
│
├── instance/
│   └── contacts.db
│
├── migrations/
│
├── static/
│
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── login.html
│   ├── register.html
│   ├── contacts.html
│   ├── add.html
│   ├── edit.html
│   ├── 404.html
│   └── 500.html
│
└── run.py
```

---

# 🗃️ Flask-Migrate

The project uses:

```text
Flask-Migrate
```

for database migrations.

This introduced the concept of managing database schema changes rather than simply deleting and recreating the database every time the models change.

The project contains:

```text
migrations/
```

which stores migration information.

The migration workflow is based around commands such as:

```bash
flask db migrate
flask db upgrade
```

---

# ⚠️ Database / Migration Learning

One of the confusing parts of the project was understanding the difference between:

```text
Model definitions
```

and:

```text
Actual database schema
```

Changing:

```python
class User(db.Model):
```

does not automatically mean the existing database has changed.

Migrations provide the mechanism for bringing the actual database schema in line with model changes.

---

# 🧯 Error Handling

Custom error pages were added for:

```text
404
500
```

The application includes:

```python
@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404
```

and:

```python
@app.errorhandler(500)
def internal_server_error(error):
    return render_template("500.html"), 500
```

The 404 page was manually tested and confirmed to work.

The 500 handler exists, although Flask's debug mode can display the development debugger instead of the custom 500 page.

---

# ✅ Form Validation

Validation was added to the major forms.

## Registration

The application checks:

```python
if not username or not password:
```

It also strips unnecessary whitespace from usernames.

Duplicate usernames are handled using:

```python
except IntegrityError:
    db.session.rollback()
```

and a flash message is displayed.

---

## Login

The login form checks that:

- Username is provided
- Password is provided
- The username exists
- The password is correct

Invalid credentials result in:

```text
Invalid username or password.
```

---

## Add Contact

The contact fields are checked before creating the database object.

```python
if not name or not phone or not email:
```

The user is redirected back to the form if validation fails.

---

## Edit Contact

The same validation is performed when editing.

This prevents empty values from being saved.

---

# 🔄 Refactoring

Towards the end of the project, repeated form-processing logic was identified.

Both `add()` and `edit()` previously contained:

```python
name = request.form["name"]
phone = request.form["phone"]
email = request.form["email"]

name = name.strip()
phone = phone.strip()
email = email.strip()
```

Instead of duplicating this logic, it was extracted into:

```python
def get_contact_data():
    name = request.form["name"].strip()
    phone = request.form["phone"].strip()
    email = request.form["email"].strip()

    return name, phone, email
```

Now both routes can simply use:

```python
name, phone, email = get_contact_data()
```

This introduced the **DRY (Don't Repeat Yourself)** principle.

The goal wasn't to abstract everything.

The goal was to remove meaningful duplication while keeping the code easy to understand.

---

# 🧪 Final Testing

Before considering the project complete, the application was manually tested through the main user flow.

The following were confirmed:

- Registration works
- Login works
- Logout works
- Adding contacts works
- Viewing contacts works
- Editing contacts works
- Deleting contacts works
- Form validation works
- Logged-out users are redirected from protected routes
- User-specific contact ownership works
- Custom 404 page works
- Navigation changes based on authentication state
- Flash messages work
- Application runs successfully after the final refactor

---

# 🧭 User Flow

## Logged Out

```text
Home
 ├── Login
 └── Register
```

## Logged In

```text
Home
 ├── Add Contact
 ├── View Contacts
 └── Logout
```

A logged-out user attempting to access protected pages is redirected to login.

---

# 🔐 Security Concepts Learned

This project is not production-ready security-wise, but it introduced several important security concepts.

### Password hashing

Passwords are hashed rather than stored directly.

### Authentication

Sessions are used to determine whether a user is logged in.

### Authorization

Database queries ensure users only access contacts belonging to their account.

### Database constraints

The username is marked:

```python
unique=True
```

so duplicate usernames cannot be created.

### Rollback

If a database operation fails:

```python
db.session.rollback()
```

is used to reset the failed transaction before continuing.

---

# 🐛 Mistakes / Problems Encountered

The project also involved several structural and conceptual problems that were useful learning experiences.

## 1. Application structure became messy

As more Flask functionality was added, keeping everything in one file became increasingly difficult.

This eventually led to separating:

```text
extensions
models
authentication routes
contact routes
application creation
```

into separate modules.

### Lesson

A project can start simple, but structure becomes increasingly important as functionality grows.

---

## 2. Blueprint endpoint names

After introducing Blueprints, old `url_for()` references stopped matching the new endpoint names.

For example, routes became namespaced:

```python
url_for("contacts.home")
```

instead of simply referring to the function name.

### Lesson

Blueprints don't just organize files. They also affect Flask's endpoint naming system.

---

## 3. Database and migration confusion

There was confusion around where the SQLite database was actually located and how Flask-SQLAlchemy resolves a relative SQLite path.

The application ultimately uses:

```text
instance/contacts.db
```

and migrations are kept separately in:

```text
migrations/
```

### Lesson

The model, migration files, and actual database are three related but distinct things.

---

## 4. Authentication vs ownership

It wasn't enough to check:

```python
@login_required
```

A logged-in user could still theoretically request another contact's ID.

The queries therefore became:

```python
Contact.query.filter_by(
    id=id,
    user_id=user_id
).first()
```

### Lesson

Being logged in does not automatically mean a user is authorized to access every resource.

---

## 5. Repeated form-processing code

The same form extraction and cleanup logic appeared in both add and edit operations.

This was eventually extracted into:

```python
get_contact_data()
```

### Lesson

Don't blindly abstract everything, but repeated logic that represents one clear responsibility is a good candidate for a helper function.

---

# 🎯 What I Deliberately Did NOT Add

The project could easily have grown indefinitely.

Possible features that were intentionally not added include:

- Contact search
- Contact categories
- Profile pages
- Password reset
- Email verification
- REST API
- Pagination
- Advanced frontend JavaScript
- Deployment configuration
- Production authentication infrastructure
- Advanced UI design

The purpose of the project was to learn the fundamentals of Flask and backend development.

Once the important concepts were covered and the application worked reliably, the project was considered complete.

---

# 🛠️ Technologies Used

- **Python**
- **Flask**
- **Jinja2**
- **SQLite**
- **Flask-SQLAlchemy**
- **Flask-Migrate**
- **Werkzeug**
- **Bootstrap**

---

# ▶️ Running the Application

Clone the repository and enter the project directory.

Install the dependencies:

```bash
pip install flask flask-sqlalchemy flask-migrate
```

Then run:

```bash
python run.py
```

The application runs in Flask's development mode.

---

# 📚 Main Concepts Practiced

| Concept | Learned |
|---|---|
| Python functions | ✅ |
| File handling | ✅ |
| JSON | ✅ |
| CRUD | ✅ |
| Flask | ✅ |
| Routing | ✅ |
| GET / POST | ✅ |
| HTML forms | ✅ |
| Jinja | ✅ |
| Template inheritance | ✅ |
| Redirects | ✅ |
| `url_for()` | ✅ |
| Flash messages | ✅ |
| SQLite | ✅ |
| SQLAlchemy | ✅ |
| Models | ✅ |
| Primary keys | ✅ |
| Foreign keys | ✅ |
| Relationships | ✅ |
| Migrations | ✅ |
| Authentication | ✅ |
| Password hashing | ✅ |
| Sessions | ✅ |
| Decorators | ✅ |
| `@wraps` | ✅ |
| Blueprints | ✅ |
| Application factory | ✅ |
| Error handlers | ✅ |
| Validation | ✅ |
| DRY / refactoring | ✅ |

---

# 🏁 Final Takeaway

The most important thing I learned from this project wasn't any individual Flask function.

It was learning how the pieces of a backend application fit together.

A request can travel through the application like this:

```text
Browser
   ↓
Flask Route
   ↓
Authentication
   ↓
Validation
   ↓
Business Logic
   ↓
SQLAlchemy
   ↓
SQLite
   ↓
Response
   ↓
Jinja Template
   ↓
Browser
```

The project started as a basic Python CLI program and ended as a structured Flask application with authentication, database persistence, relationships, protected routes, validation, error handling, and user-specific data.

That progression is the main reason this project was built.

---

## ✅ Project Status

**Completed**

The Contact Book has served its purpose as a learning project and is now considered finished.

The next step is to move on to the next stage of the Python/backend learning progression rather than continuing to add features to this application.