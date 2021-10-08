email_schema = {'type': 'string', "pattern": r"[^@]+@[^@]+\.[^@]"}
register_schema = {
    'type': 'object',
    'properties': {
        'email': email_schema,
        'password': {'type': 'string', "minLength": 4, "maxLength": 50}
    },
    'required': ['email', 'password']
}

guest_calendar_schema = {
    'type': 'object',
    'properties': {
        'guest_name': {'type': 'string', "maxLength": 20},
        'guest_email': email_schema,
        'topic': {'type': 'string', "maxLength": 200},
        'start': {'type': 'string', 'format': 'date-time'},
        'end': {'type': 'string', 'format': 'date-time'}
    },
    "required": ['guest_name', 'guest_email', 'start', 'end']
}
