import db
from convert_time import local_to_utc
from datetime import timedelta


def delete_day(params):
    """удаляет незанятые интервалы дня"""
    params_start = local_to_utc(params.date)
    params_end = params_start + timedelta(days=1)
    QUERY = " FROM Slots WHERE (?) <= start_interval AND (?) >= start_interval AND booking_id "
    with db.create_connection(params.path) as con:
        cur = con.cursor()

        cur.execute("DELETE" + QUERY + "is null", [params_start, params_end])
        cur.execute("SELECT start_interval" + QUERY + "NOT null", [params_start, params_end])
        for result in cur:
            print("""Can't delete booked interval: {}""".format(result))
