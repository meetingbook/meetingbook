import subprocess
import sys
import os

PYTHON_BINARY = sys.executable


def run_with_args(args):
    return subprocess.check_output(
        "{} cli -p db/test_main_db.sqlite {}".format(PYTHON_BINARY, args),
        shell=True, universal_newlines=True)


def run_booking_with_args(args):
    return subprocess.check_output(
        "{} tools/test-tool.py {}".format(PYTHON_BINARY, args),
        shell=True, universal_newlines=True)


def test_sanity():
    try:
        os.remove('db/test_main_db.sqlite')
    except FileNotFoundError:
        pass

    assert run_with_args("add_interval 2021-05-03T10:00 2021-05-10T11:15") == ""
    assert run_booking_with_args("2021-05-03T10:15 2021-05-03T10:45 testName test@test -t tteesstt") == ""
    assert run_with_args("get_slots -d 2021-05-03") == "2021-05-03 10:00:00 - 2021-05-04 00:00:00\n"
    assert run_with_args("get_slots -d 2021-05-03 -f booking") == "2021-05-03 10:15:00 - 2021-05-03 10:45:00\n"
    assert run_with_args(
        "get_slots -d 2021-05-03 -f free") == '''2021-05-03 10:00:00 - 2021-05-03 10:15:00\n2021-05-03 10:45:00 - 2021-05-04 00:00:00\n'''
    assert run_with_args("get_slots -w 2021-05-03") == "2021-05-03 10:00:00 - 2021-05-10 00:00:00\n"
    assert run_with_args("get_slots -w 2021-05-03 -f booking") == "2021-05-03 10:15:00 - 2021-05-03 10:45:00\n"
    assert run_with_args(
        "get_slots -w 2021-05-03 -f free") == '''2021-05-03 10:00:00 - 2021-05-03 10:15:00\n2021-05-03 10:45:00 - 2021-05-10 00:00:00\n'''
    assert run_with_args("delete_interval 2021-05-03T12:00 2021-05-08T13:15") == ""
    assert run_with_args("delete_day 2021-05-04") == ""
    assert run_with_args(
        "delete_day 2021-05-03") == "Can't delete booked interval: 2021-05-03 10:15:00\nCan't delete booked interval: 2021-05-03 10:30:00\n"
    assert run_with_args("delete_all") == 'All free slots removed\n'
