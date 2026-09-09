from flask import Flask, render_template
from .extensions import db
from flask_migrate import Migrate

from .routes.auth import auth
from .routes.contacts import contacts


def create_app():
    app = Flask(__name__, template_folder="../templates")

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///contacts.db"
    app.secret_key = "supersecretkey"

    db.init_app(app)
    Migrate(app, db)

    app.register_blueprint(auth)
    app.register_blueprint(contacts)

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("404.html"), 404

    @app.errorhandler(500)
    def internal_server_error(error):
        return render_template("500.html"), 500

    return app