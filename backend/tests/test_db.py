import db
import pytest


@pytest.fixture(scope='module')
def create_conn():
    conn = db.create_connection()
    yield conn
    conn.close()


def test_create_admininfo_table(create_conn):
    db.create_admininfo_table(create_conn)
    create_conn.execute(
        "INSERT INTO AdminInfo(email, password) values ('abc@example.com', '123456')")
    create_conn.execute(
        "INSERT INTO AdminInfo(email, password) values ('edf@example.com', 'password')")
    cursor = create_conn.execute("SELECT * FROM AdminInfo")
    result = cursor.fetchall()
    assert len(result) == 2
    assert result[0] == (1, "abc@example.com", "123456")
    assert result[1] == (2, "edf@example.com", "password")


def test_create_bookinginfo_table(create_conn):
    db.create_bookinginfo_table(create_conn)
    create_conn.execute(
        "INSERT INTO BookingInfo(name, email, topic) values ('Elon Musk', 'elon_musk@spacex.com', 'contract negotiation')")
    create_conn.execute(
        "INSERT INTO BookingInfo(name, email, topic) values ('Maye Musk', 'me@mayemusk.com', '')")
    cursor = create_conn.execute("SELECT * FROM BookingInfo")
    result = cursor.fetchall()
    assert len(result) == 2
    assert result[0] == (
        1, 'Elon Musk', 'elon_musk@spacex.com', 'contract negotiation')
    assert result[1] == (2, 'Maye Musk', 'me@mayemusk.com', '')


def test_create_slots_table(create_conn):
    db.create_bookinginfo_table(create_conn)
    db.create_slots_table(create_conn)
    create_conn.execute(
        "INSERT INTO BookingInfo(name, email, topic) values ('Elon Musk', 'elon_musk@spacex.com', 'contract negotiation')")
    booking_id = create_conn.execute(
        "SELECT id FROM BookingInfo").fetchone()[0]
    create_conn.execute("INSERT INTO slots(start_interval, booking_id) values(?, ?)",
                        ('2021-09-01T12:00', booking_id))
    create_conn.execute("INSERT INTO slots(start_interval, booking_id) values(?, ?)",
                        ('2021-09-01T12:15', booking_id))
    result = create_conn.execute("SELECT * FROM slots").fetchall()
    assert len(result) == 2
    assert result[0] == (1, '2021-09-01T12:00', 1)
    assert result[1] == (2, '2021-09-01T12:15', 1)
