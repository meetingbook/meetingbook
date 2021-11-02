from datetime import datetime
from tools.datetime_convertations import DateTime


class LinkNotFound(Exception):
    pass


class LinkHasExpired(Exception):
    pass


def ensure_valid_link(link):
    if link is None:
        raise LinkNotFound('Shareable link not found')
    elif DateTime().convert_to_datetime(link.valid_until) < datetime.utcnow():
        raise LinkHasExpired('Unauthorized - link has expired')
    return True
