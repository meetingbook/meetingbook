from tools.create_db_for_tests import create_test_app_with_db
from tools.work_with_db import get_psw_from_db


def test_get_log_psw_from_db():
    lst_log_psw = ['admin', 'Pyth0n']
    test_app = create_test_app_with_db()
    test_admin = test_app.AdminInfo(email=lst_log_psw[0], psw=lst_log_psw[1])
    test_app.db.session.add(test_admin)
    test_app.db.session.commit()
    psw_from_db = get_psw_from_db(test_app, lst_log_psw[0])
    assert psw_from_db == lst_log_psw[1]
