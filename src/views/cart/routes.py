from flask import render_template, Blueprint, flash, redirect, url_for, request
from flask_login import login_required, current_user
from src.extensions import db
from src.models import Product, Cart, CartItem
from src.views.cart.forms import CartItemForm
from src.config import Config
from os import path





TEMPLATES_FOLDER = path.join(Config.BASE_DIRECTORY, "templates", "cart")
cart_blueprint = Blueprint("cart", __name__, template_folder=TEMPLATES_FOLDER)





@cart_blueprint.route("/cart")
@login_required
def view_cart():
    # Fetch product data (name and price) from the Product model
    product_list = Product.query.all()
    product_data = [{'name': product.name, 'price': product.price} for product in product_list]

    return render_template("view_cart.html", prlist=product_data)

