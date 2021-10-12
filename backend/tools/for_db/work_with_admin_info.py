import db.models as models
import sqlalchemy
from tools.for_db.work_with_booking_settings import add_booking_settings


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
        add_booking_settings({'allowed_values': '[15]'}, {'allowed_values': '[0]'}, admin_model.id)
    except sqlalchemy.exc.IntegrityError:
        models.db.session.rollback()
        raise AdminExistsException('Such email already exists')
    finally:
        models.db.session.close()
