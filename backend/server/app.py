from flask import Flask, jsonify
from hello_json import msg_hello

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return jsonify(hello=msg_hello)


if __name__ == "__main__":
    app.run(debug=True)
