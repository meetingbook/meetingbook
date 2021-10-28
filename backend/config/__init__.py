import os


class Config():
    DEBUG = True


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI', 'sqlite:///../db/main_db.sqlite')
    MAIL_SERVER = os.environ.get('MAIL_SERVER')  # SMTP server
    MAIL_PORT = os.environ.get('MAIL_PORT')  # Port of the SMTP server
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')  # login (email) from which the letter will be sent to the administrator
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')  # password.
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True


config_settings = {
    'development': DevelopmentConfig
}
