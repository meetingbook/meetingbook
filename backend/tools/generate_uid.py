import uuid


def generate_uid() -> str:
    """Generates link_id for calendar created by Admin"""
    return str(uuid.uuid4())
