from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, RadioField, DateField, SelectField, TextAreaField, SubmitField, IntegerRangeField
from wtforms.validators import DataRequired, equal_to, length


class RegisterForm(FlaskForm):

    username = StringField("username", validators=[(DataRequired())])
    password = PasswordField("password",validators=[DataRequired(), length(min=5, max=15, message="შეიყვანეთ მინიმუმ 5 და მაქსიმუმ 15 სიმბოლო")])
    gender = RadioField("აირჩიეთ სქესი", choices=["მამრობითი","მდედრობითი"], validators=[(DataRequired())])
    birthday = DateField("დაბადების თარიღი",validators=[(DataRequired())])
    repeat_password = PasswordField("repeat password", validators=[DataRequired(),equal_to("password",message="პაროელები არ ემთხვევა")])
    submit = SubmitField("რეგისტრაცია")

class AboutForm(FlaskForm):
    texstarea = TextAreaField("უკუკავშირი. რა მოგეწონათ ან არ მოგეწონათ ჩვენთან?")
    texstareatwo = TextAreaField("რომელი ღვინო მოგეწონათ?")
    send = SubmitField("გაგზავნა")