from db import models


class AddLinkException(Exception):
    pass


def add_link(link_id, admin_id):
    try:
        link = models.Links(link_id=link_id, admin_id=admin_id)
        models.db.session.add(link)
        models.db.session.commit()
    except Exception:
        models.db.session.rollback()
        raise AddLinkException('Exception of adding a link')
    finally:
        models.db.session.close()
