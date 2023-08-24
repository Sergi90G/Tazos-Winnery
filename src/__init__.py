from flask import Flask, session
from flask_admin.menu import MenuLink
from src.config import Config
from src.extensions import db, migrate, login_manager, babel, mail
from src.models import User, Product, Role
from src.views import main_blueprint, auth_blueprint, product_blueprint
from src.commands import init_db, populate_db, send_email_command
from src.admin import admin, SecureModelView, UserView, ProductView
from flask_admin.contrib.sqla import ModelView



BLUEPRINTS = [main_blueprint, auth_blueprint, product_blueprint]
COMMANDS = [init_db, populate_db, send_email_command]

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    register_extensions(app)
    register_blueprints(app)
    register_commands(app)
    return app


def register_extensions(app):
    #flask-sqlalchemy
    db.init_app(app)

    #flask-migrate
    migrate.init_app(app, db)

    #flask-login
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    # flask-babel
    def get_locale():
        if 'locale' not in session.keys():
         session['locale'] = 'ka'
        return session['locale']


    babel.init_app(app, locale_selector=get_locale)


    #flask-admin
    admin.init_app(app)
    #amit buttonebs vamateb flask_adminshi
    admin.add_view(UserView(User, db.session))
    admin.add_view(ProductView(Product, db.session))
    admin.add_view(SecureModelView(Role, db.session))

    admin.add_link(MenuLink("Return", url="/"))

    # flask_mail
    mail.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

def register_blueprints(app):
    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint)

def register_commands(app):
    for command in COMMANDS:
        app.cli.add_command(command)



