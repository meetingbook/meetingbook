from tools.create_db_for_tests import create_test_app_with_db
from tools.work_with_db import get_psw_from_db
import db.models as db


def test_get_log_psw_from_db():
    log = 'admin'
    psw = 'Pyth0n'
    create_test_app_with_db()
    test_admin = db.AdminInfo(email=log, psw=psw)
    db.db.session.add(test_admin)
    db.db.session.commit()
    psw_from_db = get_psw_from_db(db, log)
    assert psw_from_db == psw
