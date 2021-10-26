import os


class Config():
    DEBUG = True


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI', 'sqlite:///../db/main_db.sqlite')
    MAIL_SERVER = os.environ.get('MAIL_SERVER')  # Server of the service from which the email will be sent to the admin
    MAIL_PORT = os.environ.get('MAIL_PORT')  # Port of the service from which the email will be sent to the admin
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')  # Your login (email). If you want send email in gmail use gmail login
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')  # Your password.
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True


config_settings = {
    'development': DevelopmentConfig
}
