from os import path


class Config(object):
    BASE_DIRECTORY = path.abspath(path.dirname(__file__))

    FLASK_ADMIN_SWATCH = "slate"
    UPLOAD_FOLDER = path.join(BASE_DIRECTORY, "static", "images")
    BABEL_TRANSLATION_DIRECTORIES = "../translations"

    SECRET_KEY = "abgdevztiklm"
    SERIALIZER_SALT = "nfgjkljssnins"
    SERIALIZER_SALT_PASSWORD = "fsfsggfggrewwa"
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + path.join(BASE_DIRECTORY, "database.db")


    # flask-mail
    MAIL_SERVER = "sandbox.smtp.mailtrap.io"
    MAIL_PORT = 2525
    MAIL_USERNAME = "b8c4c4a4f8e51d"
    MAIL_PASSWORD = "f276de7788774c"
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False





