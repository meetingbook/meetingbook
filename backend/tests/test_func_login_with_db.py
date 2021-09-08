from tools.create_db_for_tests import create_test_app_with_db
from tools.work_with_db import get_psw_from_db
import db.models as models


def test_get_log_psw_from_db():
    log = 'admin'
    psw = 'Pyth0n'
    create_test_app_with_db()
    test_admin = models.AdminInfo(email=log, psw=psw)
    models.db.session.add(test_admin)
    models.db.session.commit()
    psw_from_db = get_psw_from_db(log)
    assert psw_from_db == psw
