def get_psw_from_db(app, email):
    log_psw_db = app.AdminInfo.query.filter_by(email=email).first()
    psw_from_db = log_psw_db.psw
    return psw_from_db
