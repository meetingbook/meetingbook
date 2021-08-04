from types import SimpleNamespace
import delete_interval
from .func_for_test_db import clean_table_slots, create_test_table, get_test_slots, convert_from_utc_test
import add_interval as ai
import pytest


@pytest.fixture(scope='module')
def create_test_table_with_data_for_del_interval():
    params_for_add = SimpleNamespace(
        path="db/test_main_db.sqlite", start="2021-03-02T12:00", end="2021-03-02T13:15")
    clean_table_slots(params_for_add)
    create_test_table(params_for_add)
    ai.add_interval(params_for_add)


def test_delete_interval(create_test_table_with_data_for_del_interval):
    params_for_del = SimpleNamespace(
        path="db/test_main_db.sqlite", start="2021-03-02T12:00", end="2021-03-02T12:45")
    delete_interval.delete_interval(params_for_del)
    result = get_test_slots(params_for_del)
    lst = convert_from_utc_test(result)
    assert len(lst) == 1
    assert lst[0] == "2021-03-02T13:00"


def test_delete_interval_1(create_test_table_with_data_for_del_interval):
    params = SimpleNamespace(
        path="db/test_main_db.sqlite", start="2021-03-02T13:00", end="2021-03-02T13:15")
    delete_interval.delete_interval(params)
    result = get_test_slots(params)
    lst = convert_from_utc_test(result)
    assert len(lst) == 0
    assert lst == []
