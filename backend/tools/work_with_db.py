import db.models as models


def get_psw_from_db(email):
    log_psw_db = models.AdminInfo.query.filter_by(email=email).first()
    psw_from_db = log_psw_db.psw
    return psw_from_db


def push_email_psw_to_db(email, psw):
    test_admin = models.AdminInfo(email=email, psw=psw)
    models.db.session.add(test_admin)
    models.db.session.commit()
