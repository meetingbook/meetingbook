from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate

from config import config_settings
from db.models import db
from server.index import index_page
from server.admin import admin_page
from server.login import login_page
from server.swagger_ui import swaggerui_blueprint
from server.register import register_blueprint
from server.schedule_get import schedule_get
from server.schedule_post import schedule_post
from server.booking_settings import booking_settings_blueprint
from server.schedule_delete import schedule_delete
from server.guest_calendar_get import guest_calendar_get
from server.admin_calendar_get import admin_calendar_get
from server.admin_calendars_id_delete import admin_calendars_id
from server.guest_calendar_post import guest_calendar_post
from server.validation.validation_error import bad_request
from server.booking_settings_put import booking_settings_put

migrate = Migrate()


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config_settings['development'])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    migrate.init_app(app, db)
    app.register_error_handler(400, bad_request)

    app.register_blueprint(index_page)
    app.register_blueprint(admin_page)
    app.register_blueprint(swaggerui_blueprint)
    app.register_blueprint(register_blueprint)
    app.register_blueprint(schedule_get)
    app.register_blueprint(schedule_post)
    app.register_blueprint(schedule_delete)
    app.register_blueprint(login_page)
    app.register_blueprint(booking_settings_blueprint)
    app.register_blueprint(booking_settings_put)
    app.register_blueprint(admin_calendar_get)
    app.register_blueprint(admin_calendars_id)
    app.register_blueprint(guest_calendar_post)
    app.register_blueprint(guest_calendar_get)

    return app
