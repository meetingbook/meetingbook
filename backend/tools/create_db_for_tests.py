from server import app
from db.models import db


def create_test_app_with_db():
    app.app_context().push()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    db.drop_all()
    db.create_all()
    return app
