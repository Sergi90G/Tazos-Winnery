from flask_wtf import FlaskForm
from wtforms.fields import StringField, IntegerField, TextAreaField, SubmitField, FileField,  SelectField
from wtforms.validators import InputRequired, NumberRange



class CartForm(FlaskForm):
    submit = SubmitField("View Cart")



class CartItemForm(FlaskForm):
    quantity = IntegerField("Quantity", validators=[InputRequired(), NumberRange(min=1)])
    submit = SubmitField("Update Cart")