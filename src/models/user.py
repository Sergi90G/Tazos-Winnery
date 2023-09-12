from flask_login import UserMixin
from src.extensions import db
from src.models.base import BaseModel
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model, BaseModel, UserMixin):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String)
    _password = db.Column(db.String)
    gender = db.Column(db.String)
    birthday = db.Column(db.Date)
    confirmed = db.Column(db.Boolean, default=0)
    profile_image_url = db.Column(db.String(255), nullable=True)

    role_id = db.Column(db.Integer,db.ForeignKey("roles.id"))
    role = db.relationship("Role", uselist=False)





    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = generate_password_hash(value)


    def check_password(self, password):
      return check_password_hash(self.password, password)



    def __repr__(self):
       return f"შეყვანილი მონაცემებია: {self.username}{self.password}"


class Role(db.Model, BaseModel):
    __tablename__ = "roles"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)


    def __repr__(self):
        return f"{self.name}"

