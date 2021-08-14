from cli import db
from datetime import timedelta
from cli.db.convert_time import local_to_utc, utc_to_local, collapse_intervals


def get_intervals_from_db(params_path, params_filter, params_start, params_end):
    """получает объект со слотами из базы данных в зависимости от фильтра"""
    with db.create_connection(params_path) as con:
        cur = con.cursor()

        SELECT_QUERY = "SELECT start_interval FROM Slots WHERE (?) <= start_interval AND (?) >= start_interval "

        if params_filter:
            if params_filter == "free":
                SELECT_QUERY += "AND booking_id is null"
                cur.execute(SELECT_QUERY, [params_start, params_end])
            else:
                SELECT_QUERY += "AND booking_id NOT null"
                cur.execute(SELECT_QUERY, [params_start, params_end])
        else:
            cur.execute(SELECT_QUERY, [params_start, params_end])
        return cur


def get_slots(params):
    """выводит отформатированный список слотов за неделю или за день"""
    lst_of_intervals = []
    if params.week:
        param_start = local_to_utc(params.week)
        param_end = param_start + timedelta(days=7)

        intervals = get_intervals_from_db(params.path, params.filter, param_start, param_end)
        for interval_tuple in intervals:
            assert len(interval_tuple) == 1
            interval = interval_tuple[0]
            lst_of_intervals.append(utc_to_local(interval))
        lst_collapse_intervals = sorted(collapse_intervals(lst_of_intervals))
        for collapse_interval in lst_collapse_intervals:
            print(collapse_interval)
        return lst_collapse_intervals

    if params.day:
        param_start = local_to_utc(params.day)
        param_end = param_start + timedelta(days=1)

        intervals = get_intervals_from_db(params.path, params.filter, param_start, param_end)
        for interval_tuple in intervals:
            assert len(interval_tuple) == 1
            interval = interval_tuple[0]
            lst_of_intervals.append(utc_to_local(interval))
        lst_collapse_intervals = sorted(collapse_intervals(lst_of_intervals))
        for collapse_interval in lst_collapse_intervals:
            print(collapse_interval)
        return lst_collapse_intervals
