register_schema = {
    'type': 'object',
    'properties': {
        'email': {'type': 'string', "pattern": r"[^@]+@[^@]+\.[^@]"},
        'password': {'type': 'string', "minLength": 4, "maxLength": 50}
    },
    'required': ['email', 'password']
}
