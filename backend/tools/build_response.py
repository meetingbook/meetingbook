from flask import make_response, jsonify


def build_response(detail, status):
    return make_response(jsonify({'detail': detail, 'status': status}), status)
