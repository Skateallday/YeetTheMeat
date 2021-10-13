import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER='smtp.googlemail.com'
    MAIL_PORT=587
    MAIL_USE_TLS=1
    MAIL_USERNAME = 'jamfish127'
    MAIL_PASSWORD = 'pvykplcjqftugpnu'
    MAIL_DEBUG = 1
    ADMINS = ['marcinglis91@hotmail.com']
    SECURITY_EMAIL_SENDER = 'jamfish127@hotmail.com'
    POST_PER_PAGE=3
    LANGUAGES=['en', 'es']