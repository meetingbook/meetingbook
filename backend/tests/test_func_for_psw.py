import bcrypt
from tools.func_for_psw import check_psw, get_log_psw_from_header, prepare_psw_for_db


def test_get_psw_from_header():
    header = 'Basic YWRtaW46UHl0aDBu'
    log_psw = get_log_psw_from_header(header)
    assert len(log_psw) == 2
    assert log_psw[1] == 'Pyth0n'
    assert log_psw[0] == 'admin'


def test_check_psw():
    psw1 = '123'
    psw2 = '1234'
    psw_from_db = bcrypt.hashpw(psw1.encode(), bcrypt.gensalt())
    check_psw(psw1, psw_from_db)
    assert check_psw(psw1, psw_from_db) is True
    assert check_psw(psw2, psw_from_db) is False


def test_prepare_psw():
    header = 'Basic YWRtaW46UHl0aDBu'
    psw = get_log_psw_from_header(header)[1]
    hashed_psw = prepare_psw_for_db(header)
    assert check_psw(psw, hashed_psw) is True
