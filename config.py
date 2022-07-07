import os
from dotenv import load_dotenv

#basedir = os.path.join(os.path.dirname(__file__))
load_dotenv()


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    #SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL?sslmode=require') or \
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #MAIL_SERVER = os.environ.get('MAIL_SERVER')
    #MAIL_PORT = os.environ.get('MAIL_PORT')
    #MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS')
    #MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    #MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    #ADMINS = os.environ.get('ADMINS')

    # OAuth Credentials
    FACEBOOK_ID = os.environ.get('FACEBOOK_ID')
    FACEBOOK_SECRET = os.environ.get('FACEBOOK_SECRET')

    TWITTER_ID = os.environ.get('TWITTER_ID')
    TWITTER_SECRET = os.environ.get('TWITTER_SECRET')

    OAUTH_CREDENTIALS = {
        'twitter': {
            'id': os.environ.get('TWITTER_ID'),
            'secret': os.environ.get('TWITTER_SECRET')
        }
    }

    # Heroku logs
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
