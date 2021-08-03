import db
from convert_time import local_to_utc


def delete_interval(params):
    """удаляем интервал"""
    params_start = local_to_utc(params.start)
    params_end = local_to_utc(params.end)
    QUERY = " FROM Slots WHERE (?) <= start_interval AND (?) >= start_interval AND booking_id "
    if params_start.minute % 15 == 0 and params_end.minute % 15 == 0:
        with db.create_connection(params.path) as con:
            cur = con.cursor()

            cur.execute("DELETE" + QUERY + "is null", [params_start, params_end])
            cur.execute("SELECT start_interval" + QUERY + "NOT null", [params_start, params_end])
            for result in cur:
                print("""Can't delete booked interval: {}""".format(result))
    else:
        print('Введите интервал кратный 15 минутам')
