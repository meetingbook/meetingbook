class AdminDbRepository:
    def __init__(self, models):
        self._models = models

    def get_psw_from_db(self, email):
        log_psw_db = self._models.AdminInfo.query.filter_by(email=email).first()
        psw_from_db = log_psw_db.psw
        return psw_from_db

    def add_admin(self, admin):
        admin_model = self._models.AdminInfo(email=admin.get_email(), psw=admin.get_password())
        self._models.db.session.add(admin_model)
        self._models.db.session.commit()
