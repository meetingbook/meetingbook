from flask import Flask, jsonify, make_response

from admin import admin_page

app = Flask(__name__)
app.register_blueprint(admin_page)


@app.route("/", methods=["GET"])
def index():
    return jsonify({"greeting": "Hello World"})


if __name__ == "__main__":
    app.run(debug=True)
