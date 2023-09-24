from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, RadioField, DateField,  SubmitField, EmailField
from wtforms.validators import DataRequired, equal_to, length, ValidationError
from string import ascii_uppercase, ascii_lowercase, digits, punctuation
from src.models import User

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("ავტორიზაცია")

class ForResetPasswordForm(FlaskForm):
    email = EmailField("Email")
    submit = SubmitField("გამოგზავნა")

#ელფოსტით აქტივაციის კოდის ხელახლა გამოგზავნის ფორმა
class ResendKeyForm(FlaskForm):
    email = EmailField("Email")
    submit = SubmitField("გამოგზავნა")

    def validate_email(self, field):
        user = User.query.filter_by(email=field.data).first()
        if not user:
            raise ValidationError("აღნიშნული ელფოსტით მომხმარებელი არ იძებნება")

        if user.confirmed:
            raise ValidationError("მომხმარებელი გააქტიურებულია")




#პაროლისთის
class ResetPasswordForm(FlaskForm):
    new_password = PasswordField("password", validators=[DataRequired()])
    confirm_new_password = PasswordField("repeat password", validators=[(DataRequired())])
    submit = SubmitField("პაროლის შეცვლა")


class RegisterForm(FlaskForm):

    username = StringField("სახელი", validators=[(DataRequired())])
    password = PasswordField("პაროლი *",validators=[DataRequired(), length(min=5, max=15, message="შეიყვანეთ მინიმუმ 5 და მაქსიმუმ 15 სიმბოლო")])
    gender = RadioField("აირჩიეთ სქესი", choices=["მამრობითი","მდედრობითი"], validators=[(DataRequired())])
    birthday = DateField("დაბადების თარიღი",validators=[(DataRequired())])
    email = EmailField("ელ-ფოსტა")
    repeat_password = PasswordField("გაიმეორეთ პაროლი *",
                                    validators=[DataRequired(), equal_to("password", message="პაროელები არ ემთხვევა")])

    submit = SubmitField("რეგისტრაცია")

    def validate_username(self, field):
        existing_user = User.query.filter_by(username=field.data).first()
        if existing_user:
            raise ValidationError("ეს სახელი გამოყენებულია", "error")

    def validate_password(self, field):
        for character in field.data:
            contains_uppercase = character in ascii_uppercase
            contains_lowercase = character in ascii_lowercase
            contains_digits = character in digits
            contains_symbols = character in punctuation
            for character in field.data:
                if character in ascii_uppercase:
                    contains_uppercase = True

                if character in ascii_lowercase:
                    contains_lowercase = True

                if character in digits:
                    contains_digits = True

                if character in punctuation:
                    contains_symbols = True

            if not contains_uppercase:
                raise ValidationError("პაროლი უნდა შეიცავდეს დიდ ასოებს", "error")
            elif not contains_lowercase:
                raise ValidationError("პაროლი უნდა შეიცავდეს პატარა ასოებს", "error")
            elif not contains_digits:
                raise ValidationError("პაროლი უნდა შეიცავდეს ციფრებს", "error")
            elif not contains_symbols:
                raise ValidationError("პაროლი უნდა შეიცავდეს სიმბოლოებს", "error")
