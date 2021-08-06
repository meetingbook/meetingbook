from types import SimpleNamespace
from backend.tools.func_for_test_db import clean_table_slots, create_test_table
import pytest
from backend.cli import db, add_interval, get_slots
from datetime import timedelta

from backend.cli.convert_time import local_to_utc


@pytest.fixture(scope='module')
def create_test_table_with_data_for_get_slots():
    params_for_add = SimpleNamespace(path="db/test_main_db.sqlite",
                                     start="2021-03-02T00:00", end="2021-03-10T23:15")
    params_for_booking = SimpleNamespace(path="db/test_main_db.sqlite",
                                         start="2021-03-02T10:00", end="2021-03-03T11:15")
    clean_table_slots(params_for_add)
    create_test_table(params_for_add)
    add_interval.add_interval(params_for_add)
    booking(params_for_booking)


def booking(params_for_booking):
    with db.create_connection(params_for_booking.path) as con:
        cur = con.cursor()
        cur.execute("INSERT INTO BookingInfo VALUES (NULL,?,?,?)",
                    ('eduard', '@email', 'new message'))
        cur.execute("SELECT MAX(id) AS Last FROM BookingInfo")
        booking_id = cur.fetchall()
        for x in booking_id:
            res = x[0]
        params_start = local_to_utc(params_for_booking.start)
        params_end = local_to_utc(params_for_booking.end)
        while params_start < params_end:
            cur.execute(
                "UPDATE Slots SET booking_id = (?) WHERE start_interval = (?)", (res, params_start))
            params_start += timedelta(minutes=15)


def test_get_slots_week(create_test_table_with_data_for_get_slots):
    params_for_get = SimpleNamespace(path="db/test_main_db.sqlite",
                                     week="2021-03-02", filter=None, day=None)
    assert get_slots.get_slots(params_for_get)[0] == '2021-03-02 00:00:00 - 2021-03-09 00:15:00'


def test_get_slots_day(create_test_table_with_data_for_get_slots):
    params_for_get = SimpleNamespace(path="db/test_main_db.sqlite",
                                     week=None, filter=None, day="2021-03-02")
    assert get_slots.get_slots(params_for_get)[0] == '2021-03-02 00:00:00 - 2021-03-03 00:15:00'


def test_get_slots_day_free(create_test_table_with_data_for_get_slots):
    params_for_get = SimpleNamespace(path="db/test_main_db.sqlite",
                                     week=None, filter='free', day="2021-03-02")
    assert get_slots.get_slots(params_for_get)[0] == '2021-03-02 00:00:00 - 2021-03-02 10:00:00'


def test_get_slots_day_booking(create_test_table_with_data_for_get_slots):
    params_for_get = SimpleNamespace(path="db/test_main_db.sqlite",
                                     week=None, filter='booking', day="2021-03-02")
    assert get_slots.get_slots(params_for_get)[0] == '2021-03-02 10:00:00 - 2021-03-03 00:15:00'


def test_get_slots_week_free(create_test_table_with_data_for_get_slots):
    params_for_get = SimpleNamespace(path="db/test_main_db.sqlite",
                                     week="2021-03-02", filter='free', day=None)

    assert get_slots.get_slots(params_for_get)[0] == '2021-03-02 00:00:00 - 2021-03-02 10:00:00'
    assert get_slots.get_slots(params_for_get)[1] == '2021-03-03 11:15:00 - 2021-03-09 00:15:00'


def test_get_slots_week_booking(create_test_table_with_data_for_get_slots):
    params_for_get = SimpleNamespace(path="db/test_main_db.sqlite",
                                     week="2021-03-02", filter='booking', day=None)
    assert get_slots.get_slots(params_for_get)[0] == '2021-03-02 10:00:00 - 2021-03-03 11:15:00'
