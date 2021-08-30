from flask_swagger_ui import get_swaggerui_blueprint


SWAGGER_URL = '/api/docs'
API_URL = 'https://raw.githubusercontent.com/meetingbook/meetingbook/main/backend/api/meetingbook.yaml'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL
)
