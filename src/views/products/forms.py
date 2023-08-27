from flask_wtf import FlaskForm
from wtforms.fields import StringField, IntegerField, TextAreaField, SubmitField
from flask_admin.form.upload import FileUploadField

class ProductForm(FlaskForm):

    name = StringField("პროდუქტის სახელი")
    description = TextAreaField("პროდუქტის აღწერა")
    price = IntegerField("პროდუქტის ფასი")
    category = StringField("პროდუქტის კატეგორია")
    photo = FileUploadField("პროდუქტის ფოტო")
    submit = SubmitField("დამატება")