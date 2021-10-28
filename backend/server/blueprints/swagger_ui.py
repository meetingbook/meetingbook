from flask_swagger_ui import get_swaggerui_blueprint


SWAGGER_URL = '/api/docs'
API_URL = '/static/api/meetingbook.yaml'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL
)
