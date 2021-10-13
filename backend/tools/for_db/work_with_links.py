from db import models
from db.models import Links
from datetime import datetime, timedelta


class AddLinkException(Exception):
    pass


def add_link(link_id, admin_id, valid_until=(datetime.utcnow()+timedelta(days=7))):
    try:
        link = Links(link_id=link_id, admin_id=admin_id, valid_until=valid_until)
        models.db.session.add(link)
        models.db.session.commit()
    except Exception:
        models.db.session.rollback()
        raise AddLinkException('Exception of adding a link')
    finally:
        models.db.session.close()


def query_links(admin_id):
    links =