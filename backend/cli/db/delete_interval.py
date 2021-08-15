from cli import db
from cli.db.convert_time import local_to_utc, tuple_to_list


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
            tuple_to_list(cur)
            # for result in cur:
            #     result = result[0]
            #     print("""Can't delete booked interval: {}""".format(utc_to_local(result)))

    else:
        print('Введите интервал кратный 15 минутам')
