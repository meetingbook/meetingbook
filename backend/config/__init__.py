import os


class Config:
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    basedir = os.path.abspath(os.path.dirname(__file__)) + '/../db'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'main_db.sqlite')


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../db/test.sqlite'


config_settings = {
    'development': DevelopmentConfig,
    'test': TestConfig
}
