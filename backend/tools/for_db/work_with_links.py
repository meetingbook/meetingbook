from db import models
from tools.datetime_convertations import DateTime
from db.models import Links, LinksSchema, db


class LinkException(Exception):
    pass


class LinkExistsException(Exception):
    pass


def add_link(link_id, admin_id, valid_until=DateTime().utc_plus_delta(days=7)):
    try:
        link = Links(link_id=link_id, admin_id=admin_id, valid_until=valid_until)
        models.db.session.add(link)
        models.db.session.commit()
    except Exception:
        models.db.session.rollback()
        raise LinkException('Exception of adding a link')
    finally:
        models.db.session.close()


def query_links(admin_id):
    links = Links.query.filter_by(admin_id=admin_id).all()
    links_schema = LinksSchema(many=True)
    return links_schema.dump(links)


def delete_link(admin_id, link_id):
    try:
        link = Links.query.filter_by(admin_id=admin_id, link_id=link_id).first()
        db.session.delete(link)
        db.session.commit()
    except Exception:
        db.session.rollback()
        raise LinkException('Unable to delete link')
    finally:
        db.session.close()


def get_link(link_id):
    return Links.query.filter_by(link_id=link_id).first()
