from domain.repositories.admin_repository import AdminExistsException
from flask import Blueprint, request, redirect, jsonify, make_response
import bcrypt
import sqlalchemy
from email.utils import parseaddr

import db.models as models

register_blueprint = Blueprint('register_blueprint', __name__)


class InvalidRequestBodyException(Exception):
    pass


# Validation
def ensure_valid_password(password: str):
    if len(password) <= 4:
        raise InvalidRequestBodyException()


def ensure_valid_email(email: str):
    if '@' not in parseaddr(email)[1]:
        raise InvalidRequestBodyException()


# Model
def get_hashed_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def add_admin(email, password):
    try:
        admin_model = models.AdminInfo(email=email, psw=password)
        models.db.session.add(admin_model)
        models.db.session.commit()
    except sqlalchemy.exc.IntegrityError:
        models.db.session.rollback()
        raise AdminExistsException('Such email already exists')
    finally:
        models.db.session.close()


@register_blueprint.route('/registration', methods=['POST'])
def registration():
    try:
        email, password = request.get_json().values()

        ensure_valid_email(email)
        ensure_valid_password(password)
        add_admin(email, get_hashed_password(password))

        return make_response(jsonify({'detail': 'success'}), 200)
    except AdminExistsException:
        return make_response(jsonify({'detail': 'conflict'}), 409)
    except InvalidRequestBodyException:
        return make_response(jsonify({"detail": "Bad request. This is not a valid email or password is not specified"}),
                             400)
