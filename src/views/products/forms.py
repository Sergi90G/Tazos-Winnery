from flask_wtf import FlaskForm
from wtforms.fields import StringField, IntegerField, TextAreaField, SubmitField, FileField,  SelectField
from flask_admin.form.upload import FileUploadField



class ProductForm(FlaskForm):

    name = StringField("პროდუქტის სახელი")
    description = TextAreaField("პროდუქტის აღწერა")
    price = IntegerField("პროდუქტის ფასი")
    category = SelectField("პროდუქტის კატეგორია",
            choices=["თეთრი ნახევრად ტკბილი","თეთრი ცქრიალა","თეთრი მშრალი","როზე ნახევრად მშრალი",
                     "წითელი მშრალი","წითელი ნახევრად ტკბილი", "წითელი ტკბილი"])
    yearofbottling = SelectField("ღვინის ჩამოსხმის წელი", choices=["2017","2018","2019","2020","2021","2022","2023"])
    photo = FileUploadField("პროდუქტის ფოტო")
    submit = SubmitField("დამატება")