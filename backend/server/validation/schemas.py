register_schema = {
    'type': 'object',
    'properties': {
        'email': {'type': 'string', "pattern": r"[^@]+@[^@]+\.[^@]"},
        'password': {'type': 'string', "minLength": 4, "maxLength": 50}
    },
    'required': ['email', 'password']
}

booking_settings_schema = {
    'type': 'object',
    'properties': {
        'duration': {'type': 'object',
                     'properties': {
                         'allowed_values': {'type': 'array'}
                     }},
        'start_time': {'type': 'object',
                       'properties': {
                           'allowed_values': {'type': 'array'}
                       }}},
    'required': ['duration', 'start_time']
}
