# datetime_schema =
guest_calendar_schema = {
    "type": "object",
    "properties": {
        "guest_name": {"type": "string"},
        "guest_email": {"type": "string"},
        "topic": {"type": "string"},
        "start": {"type": "string", "pattern": "d{4}\-d{2}\-d{2}\Td{2}\:d{2}\:d{2}\.d{3}\Z"},
        "end": {"type": "string", "pattern": "d{4}\-d{2}\-d{2}\Td{2}\:d{2}\:d{2}\.d{3}\Z"}
    },
    "required": ["guest_name", "guest_email", "start", "end"]
}

register_schema = {
    'type': 'object',
    'properties': {
        'email': {'type': 'string', "pattern": "[^@]+@[^@]+\.[^@]"},
        'password': {'type': 'string', "minLength": 4, "maxLength": 50}
    },
    'required': ['email', 'password']
}
