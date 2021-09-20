class AdminDbRepository:
    def __init__(self, models, email, password):
        self.__models = models
        self.__email = email
        self.__password = password

    def get_psw_from_db(self):
        log_psw_db = self.__models.AdminInfo.query.filter_by(email=self.__email).first()
        psw_from_db = log_psw_db.psw
        return psw_from_db

    def add_admin(self):
        admin = self.__models.AdminInfo(email=self.__email, psw=self.__password)
        self.__models.db.session.add(admin)
        self.__models.db.session.commit()
