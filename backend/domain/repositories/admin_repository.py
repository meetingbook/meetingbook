import db.models as models
import sqlalchemy


class AdminExistsException(Exception):
    pass


class AdminDbRepository(AdminExistsException):

    def get_psw_from_db(self, email):
        log_psw_db = models.AdminInfo.query.filter_by(email=email).first()
        psw_from_db = log_psw_db.psw
        return psw_from_db

    def add_admin(self, admin):
        try:
            admin_model = models.AdminInfo(email=admin.get_email(), psw=admin.get_password())
            models.db.session.add(admin_model)
            models.db.session.commit()
        except sqlalchemy.exc.IntegrityError:
            models.db.session.rollback()
            raise AdminExistsException('Such email already exists')
        finally:
            models.db.session.close()
