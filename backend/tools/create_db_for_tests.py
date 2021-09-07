import server.app as app


def create_test_app_with_db():
    app.app.config['TESTING'] = True
    app.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.db.create_all()
    return app
