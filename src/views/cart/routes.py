from flask import render_template, Blueprint, flash, redirect, url_for
from flask_login import login_required, current_user
from src.models import Product, Cart, CartItem
from flask_login import login_required
from src.views.cart.forms import CartForm, CartItemForm
from src.models import Product
from src.config import Config
from os import path




TEMPLATES_FOLDER = path.join(Config.BASE_DIRECTORY, "templates", "products")
cart_blueprint = Blueprint("cart", __name__, template_folder=TEMPLATES_FOLDER)


@cart_blueprint.route("/cart")
@login_required
def view_cart():
    user_cart = Cart.query.filter_by(user_id=current_user.id).first()
    if user_cart:
        cart_items = CartItem.query.filter_by(cart_id=user_cart.id).all()
    else:
        cart_items = []

    return render_template("view_cart.html", cart_items=cart_items, user_cart=user_cart)

@cart_blueprint.route("/add_to_cart/<int:product_id>")
@login_required
def add_to_cart(product_id):
    product = Product.query.get(product_id)
    user_cart = Cart.query.filter_by(user_id=current_user.id).first()

    if not user_cart:
        # Create a new cart for the user if they don't have one
        user_cart = Cart(user_id=current_user.id)
        user_cart.create()

    # Check if the product is already in the user's cart
    existing_cart_item = CartItem.query.filter_by(cart_id=user_cart.id, product_id=product_id).first()

    if existing_cart_item:
        # If the product is in the cart, increase the quantity
        existing_cart_item.quantity += 1
    else:
        # If not, create a new cart item
        new_cart_item = CartItem(cart_id=user_cart.id, product_id=product_id)
        new_cart_item.create()

    flash("Product added to cart successfully.")
    return redirect(url_for("cart.view_cart"))

@cart_blueprint.route("/remove_from_cart/<int:cart_item_id>")
@login_required
def remove_from_cart(cart_item_id):
    cart_item = CartItem.query.get(cart_item_id)

    if cart_item:
        if cart_item.cart.user_id == current_user.id:
            if cart_item.quantity > 1:
                # If there is more than one of the item, decrease the quantity
                cart_item.quantity -= 1
            else:
                # If there is only one, remove the item from the cart
                cart_item.delete()
                flash("Product removed from cart.")
        else:
            flash("You don't have permission to remove this item from the cart.")
    else:
        flash("Cart item not found.")

    return redirect(url_for("cart.view_cart"))

@cart_blueprint.route("/checkout")
@login_required
def checkout():
    user_cart = Cart.query.filter_by(user_id=current_user.id).first()
    if user_cart:
        cart_items = CartItem.query.filter_by(cart_id=user_cart.id).all()
    else:
        cart_items = []

    # You can add logic for processing the checkout here
    # For example, creating an order and clearing the cart

    return render_template("checkout.html", cart_items=cart_items, user_cart=user_cart)
