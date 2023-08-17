from flask.cli import with_appcontext
import click
from src.extensions import db
from src.models import User, Role, Product
from src.utils import send_email




@click.command("init_db")
@with_appcontext
def init_db():
    click.echo("Creating DB")
    db.drop_all()
    db.create_all()
    click.echo("DB Created")


@click.command("populate_db")
@with_appcontext
def populate_db():
    click.echo("Creating products")
    for index in range(10):
        product = Product(name=f"Product {index}", description=f"აღწერა product {index}-ისთვის", price=500 + index)
        product.create(commit=False)
    Product.save()


    roles = ["admin", "moderator", "member"]
    for role in roles:
        new_role = Role(name=role)
        new_role.create()

    admin_user = User(username="admin", password="Password123!", role_id=1)
    admin_user.create()

    click.echo("Products created")

@click.command("send_email")
@with_appcontext
def send_email_command():
    send_email("სატესტო მეილი", "ეს არის სატესტო მეილი ", ["test@yahoo.com"])
    click.echo("load")
    click.echo("done")



