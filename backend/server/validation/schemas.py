email_schema = {'type': 'string', "pattern": r"[^@]+@[^@]+\.[^@]"}
datetime_schema = {'type': 'string', 'pattern': r'd{4}\-d{2}\-d{2}\Td{2}\:d{2}\:d{2}\.d{3}\Z'}
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
        'start': datetime_schema,
        'end': datetime_schema
    },
    "required": ['guest_name', 'guest_email', 'start', 'end']
}
