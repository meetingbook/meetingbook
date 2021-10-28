from types import SimpleNamespace
from backend.tools.for_test.func_for_test_db import clean_table_slots, create_test_table, get_test_slots, convert_from_utc_test
from cli.db import delete_day, add_interval
import pytest


@pytest.fixture(scope='module')
def create_test_table_with_data_for_del_day():
    params_for_add = SimpleNamespace(
        path="db/test_main_db.sqlite", start="2021-03-02T22:45", end="2021-03-03T03:15")
    clean_table_slots(params_for_add)
    create_test_table(params_for_add)
    add_interval.add_interval(params_for_add)


def test_delete_day(create_test_table_with_data_for_del_day):
    params = SimpleNamespace(path="db/test_main_db.sqlite", date="2021-03-02")
    delete_day.delete_day(params)
    result = get_test_slots(params)
    lst = convert_from_utc_test(result)
    assert len(lst) == 12
    assert lst[0] == '2021-03-03T00:15'
    assert lst[6] == '2021-03-03T01:45'
    assert lst[11] == '2021-03-03T03:00'
