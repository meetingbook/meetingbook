import db
from convert_time import local_to_utc, utc_to_local_format
from datetime import timedelta


def add_interval(params):
    """Добавление интервала в базу данных"""
    params_start = local_to_utc(params.start)
    params_end = local_to_utc(params.end)
    if params_start.minute % 15 == 0 and params_end.minute % 15 == 0:
        with db.create_connection(params.path) as con:
            cur = con.cursor()
            insert_list = []
            while params_start < params_end:
                cur.execute("SELECT start_interval FROM Slots WHERE start_interval == (?)", [params_start])
                interval_list = cur.fetchall()
                if len(interval_list) > 0:
                    assert len(interval_list) == 1
                    interval_tuple = interval_list[0]
                    assert len(interval_tuple) == 1
                    interval = interval_tuple[0]
                    finish_interval = params_start + timedelta(minutes=15)
                    print('interval ({} - {}) already exist'.format(utc_to_local_format(interval),
                                                                    utc_to_local_format(finish_interval.isoformat())))
                else:
                    insert_list.append((params_start,))

                params_start += timedelta(minutes=15)
            cur.executemany("INSERT INTO Slots (start_interval) VALUES (?)", insert_list)
    else:
        mes = 'Введите интервал кратный 15 минутам'
        print(mes)
        return mes
