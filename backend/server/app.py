from flask import Flask, jsonify
from server.hello_json import msg_hello
from server.admin import admin_page

app = Flask(__name__)
app.register_blueprint(admin_page)


@app.route("/", methods=["GET"])
def index():
    return jsonify(msg_hello)


if __name__ == "__main__":
    app.run(debug=True)
