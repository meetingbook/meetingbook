from flask import jsonify, Blueprint

index_page = Blueprint('index_page', __name__)

msg_hello = {
    "greeting": "Hello World"
}


@index_page.route("/", methods=["GET"])
def index():
    return jsonify(msg_hello)
