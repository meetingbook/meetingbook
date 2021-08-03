import db


def delete_all(params):
    """удаляет все незанятые интервалы"""
    with db.create_connection(params.path) as con:
        cur = con.cursor()

        cur.execute("DELETE FROM Slots WHERE booking_id is null")