import db.models as models


def get_psw_from_db(email):
    log_psw_db = models.AdminInfo.query.filter_by(email=email).first()
    psw_from_db = log_psw_db.psw
    return psw_from_db