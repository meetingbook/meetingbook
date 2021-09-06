from flask import Flask
from flask_migrate import Migrate

from config import config_settings
from db.models import db
from server.index import index_page
from server.admin import admin_page
from server.swagger_ui import swaggerui_blueprint

migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config_settings['development'])
    app.register_blueprint(index_page)
    app.register_blueprint(admin_page)
    app.register_blueprint(swaggerui_blueprint)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    return app
