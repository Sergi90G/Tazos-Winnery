from src.extensions import db
from src.models.base import BaseModel
from src.models import User, Product



class Cart(db.Model, BaseModel):
    __tablename__ = "carts"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.ForeignKey("user.id"), nullable=False)
    user = db.relationship(User, backref="cart", uselist=False)

    def __repr__(self):
        return f"Cart for user: {self.user.username}"


class CartItem(db.Model, BaseModel):
    __tablename__ = "cart_items"

    id = db.Column(db.Integer, primary_key=True)
    cart_id = db.Column(db.ForeignKey("carts.id"), nullable=False)
    cart = db.relationship(Cart, backref="items")
    product_id = db.Column(db.ForeignKey("products.id"), nullable=False)
    product = db.relationship(Product, uselist=False)
    quantity = db.Column(db.Integer, default=1)

    def __repr__(self):
        return f"CartItem: {self.product.name} (Quantity: {self.quantity})"