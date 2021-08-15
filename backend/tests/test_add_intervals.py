from types import SimpleNamespace

from backend.tools.func_for_test_db import clean_table_slots, create_test_table, get_test_slots, convert_from_utc_test
import pytest

from cli.db import add_interval


@pytest.fixture(scope='module')
def create_test_table_for_add_interval():
    params = SimpleNamespace(
        path="db/test_main_db.sqlite")
    clean_table_slots(params)
    create_test_table(params)


def test_add_interval(create_test_table_for_add_interval):
    params = SimpleNamespace(path="db/test_main_db.sqlite",
                             start="2021-03-02T12:00", end="2021-03-02T13:15")
    add_interval.add_interval(params)
    result = get_test_slots(params)
    lst = convert_from_utc_test(result)
    assert len(lst) == 5
    assert lst[0] == '2021-03-02T12:00'
    assert lst[1] == '2021-03-02T12:15'


def test_add_interval_negative(create_test_table_for_add_interval):
    params = SimpleNamespace(path="db/test_main_db.sqlite",
                             start="2021-03-01T12:10", end="2021-03-01T13:15")
    assert add_interval.add_interval(
        params) == "Введите интервал кратный 15 минутам"
