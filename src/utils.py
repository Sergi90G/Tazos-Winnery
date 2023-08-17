from flask_mail import Message
from src.extensions import mail
from itsdangerous import URLSafeTimedSerializer
from src.config import Config


def send_email(subject, text, recipients):
    message = Message(subject=subject, html=text, recipients=recipients, sender="sergo.gogishvili.1@iliauni.edu.ge")
    mail.send(message)

# მომხმარებლის ელფოსტა გადაეცემა მხოლოდ და იქმნება აქტივაციის გასაღები
def create_key(user_email):
    serializer = URLSafeTimedSerializer(Config.SECRET_KEY)
    key = serializer.dumps(user_email, salt=Config.SERIALIZER_SALT)
    return key

# აქ ვადასტურებთ რომ მომხმარებლისგან გადმოცემული გასაღები არის თუ არა სწორი და არ არის ვადაგასული
def confirm_key(activation_key):
    serializer = URLSafeTimedSerializer(Config.SECRET_KEY)
    try:
        email = serializer.loads(activation_key, salt=Config.SERIALIZER_SALT, max_age=120)
    except:
        return False
    else:
        return email

def create_password_reset_key(user_email):
    serializer = URLSafeTimedSerializer(Config.SECRET_KEY)
    key = serializer.dumps(user_email, salt=Config.SERIALIZER_SALT_PASSWORD)
    return key

def confirm_password_reset_key(reset_key):
    serializer = URLSafeTimedSerializer(Config.SECRET_KEY)
    try:
        email = serializer.loads(reset_key, salt=Config.SERIALIZER_SALT_PASSWORD, max_age=340)
    except:
        return False
    else:
        return email