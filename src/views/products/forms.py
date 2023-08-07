from flask_wtf import FlaskForm
from wtforms.fields import StringField, IntegerField, TextAreaField, SubmitField, FileField

class ProductForm(FlaskForm):

    name = StringField("პროდუქტის სახელი")
    description = TextAreaField("პროდუქტის აღწერა")
    price = IntegerField("პროდუქტის ფასი")
    photo = FileField("პროდუქტის ფოტო")
    submit = SubmitField("პროდუქტის დამატება")