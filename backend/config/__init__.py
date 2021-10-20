import os


class Config():
    DEBUG = True


class DevelopmentConfig(Config):
    basedir = os.path.abspath(os.path.dirname(__file__)) + '/../db'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'main_db.sqlite')
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = 'meetingbookemail@gmail.com'
    MAIL_PASSWORD = 'Meetingb00k'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True


config_settings = {
    'development': DevelopmentConfig
}
