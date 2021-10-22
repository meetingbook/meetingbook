email_schema = {'type': 'string', "pattern": r"[^@]+@[^@]+\.[^@]"}
datetime_schema = {'type': 'string', 'format': 'date-time', "pattern":
                   r'^(-?(?:[1-9][0-9]*)?[0-9]{4})-(1[0-2]|0[1-9])-(3[01]|0[1-9]|[12][0-9])'
                   r'T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\.[0-9]+)?(Z|[+-](?:2[0-3]|[01][0-9]):[0-5][0-9])?$'}
register_schema = {
    'type': 'object',
    'properties': {
        'email': email_schema,
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

guest_calendar_schema = {
    'type': 'object',
    'properties': {
        'guest_name': {'type': 'string', "minLength": 1, "maxLength": 20},
        'guest_email': email_schema,
        'topic': {'type': 'string', "maxLength": 200},
        'start': datetime_schema,
        'end': datetime_schema
    },
    "required": ['guest_name', 'guest_email', 'start', 'end']
}

calendar_link_schema = {
    'type': 'object',
    'properties':
        {
            'data': {
                'valid_until': datetime_schema
            }
        }
}
