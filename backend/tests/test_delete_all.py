from types import SimpleNamespace
from backend.tools.for_test.func_for_test_db import clean_table_slots, create_test_table, get_test_slots, convert_from_utc_test
import pytest

from cli.db import delete_all, add_interval


@pytest.fixture(scope='module')
def create_test_table_with_data_for_del_all():
    params_for_add = SimpleNamespace(
        path="db/test_main_db.sqlite", start="2021-03-02T22:45", end="2021-03-03T03:15")
    clean_table_slots(params_for_add)
    create_test_table(params_for_add)
    add_interval.add_interval(params_for_add)


def test_delete_day(create_test_table_with_data_for_del_all):
    params = SimpleNamespace(path="db/test_main_db.sqlite")
    delete_all.delete_all(params)
    result = get_test_slots(params)
    lst = convert_from_utc_test(result)
    assert len(lst) == 0
    assert lst == []
