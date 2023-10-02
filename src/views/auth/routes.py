from flask import Blueprint, render_template, flash, redirect, url_for, request
from os import path

from src import db
from src.config import Config
from src.views.auth.forms import RegisterForm, LoginForm, ResendKeyForm, ResetPasswordForm, ForResetPasswordForm
from src.models import User
from flask_login import login_user, logout_user
from src.utils import send_email, create_key, confirm_key, confirm_password_reset_key, create_password_reset_key
from flask_babel import _
from werkzeug.security import generate_password_hash

TEMPLATES_FOLDER = path.join(Config.BASE_DIRECTORY, "templates", "auth")
auth_blueprint = Blueprint("auth", __name__, template_folder=TEMPLATES_FOLDER)


@auth_blueprint.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User()
        form.populate_obj(user)
        user.role_id = 3
        user.create()

        activation_key = create_key((form.email.data))
        html = render_template("_activation_message.html", activation_key=activation_key)
        send_email("რეგისტრაცია საიტზე", html, [form.email.data])
        flash(_('აქტივაციის ლინკი გამოგზავნილია'), 'success')
        return redirect(url_for("main.index"))

    if form.errors:
        for errors in form.errors.values():
            for error in errors:
                flash(error)
    return render_template("register.html", form=form)


@auth_blueprint.route("/resend_key", methods=["GET", "POST"])
def resend_key():
    form = ResendKeyForm()
    if form.validate_on_submit():
        activation_key = create_key(form.email.data)
        html = render_template("_resend_key_message.html", activation_key=activation_key)
        send_email("მეილის აქტივაცია", html, [form.email.data])

        flash(_('* აქტივაციის კოდი გამოგზავნილია'), 'success')
        return redirect(url_for("main.index"))

    if form.errors:
        for errors in form.errors.values():
            for error in errors:
                flash(error)

    return render_template("resend_key.html", form=form)


@auth_blueprint.route("/confirm_email/<activation_key>")
def confirm_email(activation_key):
    email = confirm_key(activation_key)
    if not email:
        flash(_('* აქტივაციის კოდი არასწორია ან გაუვიდა ვადა'), 'error')
        return redirect(url_for("auth.register"))

    user = User.query.filter_by(email=email).first()
    if user.confirmed:
        flash(_('* მომხმარებელი უკვე გააქტიურებულია'), 'error')
        return redirect(url_for("auth.login"))

    user.confirmed = True
    user.save()
    login_user(user)
    return redirect(url_for("main.index"))


@auth_blueprint.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():

        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            flash(_('ეს მომხმარებელი ვერ მოიძებნა'), 'error')
            return redirect(url_for("auth.login"))

        if not user.confirmed:
            flash(_('ელ-ფოსტა არ დადასტურდა'), 'error')
            return redirect(url_for("auth.login"))

        if user.check_password(form.password.data):
            flash(_('თქვენ წარმატებით გაიარეთ ავტორიზაცია!'), 'success')
            login_user(user)
            next = request.args.get("next")
            if next:
                return redirect(next)
            else:
                return redirect(url_for("main.index"))
        else:
            flash(_('პაროლი არასწორია'), 'error')

    return render_template("login.html", form=form)


@auth_blueprint.route("/logout")
def logout():
    logout_user()
    flash(_('თქვენ გამოხვედით საიტიდან'), 'success')
    return redirect(url_for("main.index"))


@auth_blueprint.route("/for_reset_password", methods=["GET", "POST"])
def for_reset_password():
    form = ForResetPasswordForm()
    if form.validate_on_submit():
        reset_key = create_password_reset_key(form.email.data)
        html = render_template("_reset_password_message.html", reset_key=reset_key)
        send_email("პაროლის აღდგენა", html, [form.email.data])

        flash(_('* პაროლის აღდგენის კოდი გამოგზავნილია'), 'success')
        return redirect(url_for("main.index"))

    if form.errors:
        for errors in form.errors.values():
            for error in errors:
                flash(error)

    return render_template("for_reset_password.html", form=form)


@auth_blueprint.route("/reset_password/<reset_key>", methods=["GET", "POST"])
def reset_password(reset_key):
    email = confirm_password_reset_key(reset_key)
    if not email:
        flash(_('აქტივაციის კოდი არასწორია ან გაუვიდა ვადა'), 'error')
        return redirect(url_for("auth.register"))

    user = User.query.filter_by(email=email).first()
    if user is None:
        flash(_('მომხმარებელი ვერ მოიძებნა'), 'error')
        return redirect(url_for("main.index"))

    form = ResetPasswordForm()
    if form.validate_on_submit():

      user.password = form.new_password.data
      db.session.commit()

      login_user(user)
      flash(_('პაროლი შეიქმნა წარმატებით'), 'success')
      return redirect(url_for("main.index", form=form, reset_key=reset_key))

    return render_template("reset_password.html", form=form)
