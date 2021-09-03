from flask import Flask, jsonify
from server.hello_json import msg_hello
from server.admin import admin_page
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os


app = Flask(__name__)
app.register_blueprint(admin_page)

basedir = os.path.abspath(os.path.dirname("db/"))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'main_db.sqlite')

db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route("/", methods=["GET"])
def index():
    return jsonify(msg_hello)


if __name__ == "__main__":
    app.run(debug=True)
