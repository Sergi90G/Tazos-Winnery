from flask_mail import Message
from src.extensions import mail
from itsdangerous import URLSafeTimedSerializer
from src.config import Config


def send_email(subject, text, recipients):
    message = Message(subject=subject, html=text, recipients=recipients, sender="testagain@yahoo.com")
    mail.send(message)

def create_key(user_email):
    serializer = URLSafeTimedSerializer(Config.SECRET_KEY)
    key = serializer.dumps(user_email, salt=Config.SERIALIZER_SALT)
    return key

def confirm_key(activation_key):
    serializer = URLSafeTimedSerializer(Config.SECRET_KEY)
    try:
        email = serializer.loads(activation_key, salt=Config.SERIALIZER_SALT, max_age=120)
    except:
        return False
    else:
        return email
