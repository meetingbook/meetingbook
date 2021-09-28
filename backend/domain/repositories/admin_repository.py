import db.models as models


class AdminDbRepository:

    def get_psw_from_db(self, email):
        log_psw_db = models.AdminInfo.query.filter_by(email=email).first()
        psw_from_db = log_psw_db.psw
        return psw_from_db

    def add_admin(self, admin):
        admin_model = models.AdminInfo(email=admin.get_email(), psw=admin.get_password())
        models.db.session.add(admin_model)
        models.db.session.commit()
