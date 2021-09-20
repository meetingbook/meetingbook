from tools.func_for_psw import check_psw, get_log_psw_from_header, prepare_psw_for_db


def test_get_psw_from_header():
    header = 'Basic YWRtaW46UHl0aDBu'
    log_psw = get_log_psw_from_header(header)
    assert len(log_psw) == 2
    assert log_psw[1] == 'Pyth0n'
    assert log_psw[0] == 'admin'


def test_prepare_and_check_psw():
    psw = 'Pyth0n'
    psw_2 = 'psw_2'
    hashed_psw = prepare_psw_for_db(psw)
    hashed_psw2 = prepare_psw_for_db(psw_2)
    assert check_psw(psw, hashed_psw) is True
    assert check_psw(psw_2, hashed_psw2) is True
    assert check_psw(psw_2, hashed_psw) is False
    assert check_psw(psw, hashed_psw2) is False
