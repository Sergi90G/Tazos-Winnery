from flask_wtf import FlaskForm
from wtforms.fields import  TextAreaField, SubmitField




class AboutForm(FlaskForm):
    texstarea = TextAreaField("უკუკავშირი. რა მოგეწონათ ან არ მოგეწონათ ჩვენთან?")
    texstareatwo = TextAreaField("რომელი ღვინო მოგეწონათ?")
    send = SubmitField("გაგზავნა")