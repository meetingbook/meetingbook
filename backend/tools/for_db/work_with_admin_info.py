import db.models as models
import sqlalchemy


class AdminExistsException(Exception):
    pass


def get_psw_from_db(email):
    log_psw_db = models.AdminInfo.query.filter_by(email=email).first()
    psw_from_db = log_psw_db.psw
    return psw_from_db


def add_admin(email, password):
    try:
        admin_model = models.AdminInfo(email=email, psw=password)
        models.db.session.add(admin_model)
        models.db.session.commit()
    except sqlalchemy.exc.IntegrityError:
        models.db.session.rollback()
        raise AdminExistsException('Such email already exists')
    finally:
        models.db.session.close()


def get_admin_id(email):
    return models.AdminInfo.query.filter_by(email=email).first().id
