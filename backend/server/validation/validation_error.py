from flask import make_response, jsonify
from jsonschema import ValidationError


def bad_request(error):
    if isinstance(error.description, ValidationError):
        original_error = error.description
        return make_response(jsonify({'status': 400, 'detail': original_error.message}), 400)
    # handle other "Bad Request"-errors
    return error
