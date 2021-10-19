import os
import dotenv

dotenv.load_dotenv('.env')


class Config:
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI', 'sqlite:///../db/main_db.sqlite')


config_settings = {
    'development': DevelopmentConfig
}
