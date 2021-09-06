import os


class Config():
    DEBUG = True


class DevelopmentConfig(Config):
    basedir = os.path.abspath(os.path.dirname("db/"))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'main_db.sqlite')


config_settings = {
    'development': DevelopmentConfig
    }
