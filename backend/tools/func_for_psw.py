import bcrypt
import base64


def get_log_psw_from_header(header):
    base64_log_psw = header.split(' ')[1]
    decoded_log_psw = base64.b64decode(base64_log_psw.encode('utf-8')).decode('utf-8')
    lst_decode_log_psw = decoded_log_psw.split(':')
    return lst_decode_log_psw


def check_psw(decoded_psw, psw_from_db):
    check = bcrypt.checkpw(decoded_psw.encode(), psw_from_db)
    return check


def prepare_psw_for_db(header):
    log_psw = get_log_psw_from_header(header)
    psw = log_psw[1]
    hashed_psw = bcrypt.hashpw(psw.encode(), bcrypt.gensalt())
    return hashed_psw
