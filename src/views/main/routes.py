from flask import render_template, Blueprint, flash, url_for, session, redirect
from os import path

from src.views.main.forms import  AboutForm
from src.config import Config

TEMPLATES_FOLDER = path.join(Config.BASE_DIRECTORY, "templates", "main")
main_blueprint = Blueprint("main", __name__, template_folder=TEMPLATES_FOLDER)


@main_blueprint.route("/", methods=["GET", "POST"])
def index():

    return render_template("index.html", user_type="admin")

@main_blueprint.route("/profile", methods=["GET", "POST"])
def profile():

    return render_template("profile.html")

@main_blueprint.route("/about", methods=['GET','POST'])
def about():
    form = AboutForm()
    text = None

    if form.validate_on_submit():
        text = form.texstarea.data


    return render_template("about.html", form=form,  text=text)

@main_blueprint.route("/change_language")
def change_language():
    if session['locale'] == 'ka':
        session['locale'] = 'en'
    else:
        session['locale'] = 'ka'

    return redirect(url_for('main.index'))