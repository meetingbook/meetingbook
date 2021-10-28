from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate

from config import config_settings
from db.models import db
from server.blueprints.index import index_page
from server.blueprints.admin import admin_page
from server.blueprints.login import login_page
from server.blueprints.swagger_ui import swaggerui_blueprint
from server.blueprints.register import register_blueprint
from server.blueprints.schedule_get import schedule_get
from server.blueprints.schedule_post import schedule_post
from server.blueprints.booking_settings import booking_settings_blueprint
from server.blueprints.schedule_delete import schedule_delete
from server.blueprints.guest_calendar_get import guest_calendar_get
from server.blueprints.admin_calendar_get import admin_calendar_get
from server.blueprints.admin_calendars_id_delete import admin_calendars_id
from server.blueprints.guest_calendar_post import guest_calendar_post
from server.validation.validation_error import bad_request
from server.blueprints.booking_settings_put import booking_settings_put
from server.blueprints.calendars_post_for_admin import calendars_post
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
    app.register_blueprint(calendars_post)
    return app
