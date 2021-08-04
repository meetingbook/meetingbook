import db
import convert_time


def create_test_table(params):
    con = db.create_connection(params.path)
    db.create_slots_table(con)
    db.create_admininfo_table(con)
    db.create_bookinginfo_table(con)


def clean_table_slots(params):
    with db.create_connection(params.path) as con:
        cur = con.cursor()
        cur.execute("""DROP TABLE IF EXISTS Slots;""")


def get_test_slots(params):
    with db.create_connection(params.path) as con:
        cur = con.cursor()
        a = cur.execute(
            "SELECT start_interval FROM Slots")
        return a.fetchall()


def convert_from_utc_test(result):
    lst = []
    for interval_tuple in result:
        interval = interval_tuple[0]
        dt = convert_time.utc_to_local(interval)
        lst.append(dt.strftime('%Y-%m-%dT%H:%M'))
    return lst
