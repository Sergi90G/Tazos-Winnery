from flask import render_template, Blueprint, flash, url_for, session, redirect, request
from os import path
from src.views.main.forms import AboutForm
from src.config import Config
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from src.extensions import db
from src.models import User

TEMPLATES_FOLDER = path.join(Config.BASE_DIRECTORY, "templates", "main")
main_blueprint = Blueprint("main", __name__, template_folder=TEMPLATES_FOLDER)


@main_blueprint.route("/", methods=["GET", "POST"])
def index():

    return render_template("index.html", user_type="admin")


@main_blueprint.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    if request.method == "POST":
        # Handle profile image upload
        if "profile_image" in request.files:
            file = request.files["profile_image"]
            if file.filename != "":
                filename = secure_filename(file.filename)
                file.save(path.join(Config.UPLOAD_FOLDER, filename))
                current_user.profile_image_url = url_for("static", filename=f"images/{filename}")
                #დათაბაზაში დამატების ფუნქციონალი გავაკეთო
                flash("Profile image updated successfully.", 'success')

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