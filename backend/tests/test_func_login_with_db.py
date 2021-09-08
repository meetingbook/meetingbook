from tools.create_db_for_tests import create_test_app_with_db
from tools.work_with_db import get_psw_from_db


def test_get_log_psw_from_db():
    log = 'admin'
    psw = 'Pyth0n'
    test_app = create_test_app_with_db()
    test_admin = test_app.AdminInfo(email=log, psw=psw)
    test_app.db.session.add(test_admin)
    test_app.db.session.commit()
    psw_from_db = get_psw_from_db(test_app, log)
    assert psw_from_db == psw
