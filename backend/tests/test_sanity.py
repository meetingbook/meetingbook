import subprocess
import sys
import os
from cli.db.convert_time import utc_to_local, local_to_utc

PYTHON_BINARY = sys.executable


def run_with_args(args):
    return subprocess.check_output(
        "{} cli -p db/test_main_db.sqlite {}".format(PYTHON_BINARY, args),
        shell=True)


def run_booking_with_args(args):
    return subprocess.check_output(
        "{} tools/test-tool.py {}".format(PYTHON_BINARY, args),
        shell=True)


def time_in_utc_then_in_local(x):
    return utc_to_local(str(local_to_utc(x)))


def test_sanity():
    try:
        os.remove('db/test_main_db.sqlite')
    except FileNotFoundError:
        pass

    assert run_with_args("add_interval 2021-05-03T10:00 2021-05-10T11:15") == b""
    assert run_booking_with_args("2021-05-03T10:15 2021-05-03T10:45 testName test@test -t tteesstt") == b""
    assert run_with_args("get_slots -d 2021-05-03") == b'2021-05-03 10:00:00 - 2021-05-04 00:15:00\r\n'
    assert run_with_args("get_slots -d 2021-05-03 -f booking") == b"2021-05-03 10:15:00 - 2021-05-03 10:45:00\r\n"
    assert run_with_args(
        "get_slots -d 2021-05-03 -f free") == b'''2021-05-03 10:00:00 - 2021-05-03 10:15:00\r\n2021-05-03 10:45:00 - 2021-05-04 00:15:00\r\n'''
    assert run_with_args("get_slots -w 2021-05-03") == b"2021-05-03 10:00:00 - 2021-05-10 00:15:00\r\n"
    assert run_with_args("get_slots -w 2021-05-03 -f booking") == b"2021-05-03 10:15:00 - 2021-05-03 10:45:00\r\n"
    assert run_with_args(
        "get_slots -w 2021-05-03 -f free") == b'''2021-05-03 10:00:00 - 2021-05-03 10:15:00\r\n2021-05-03 10:45:00 - 2021-05-10 00:15:00\r\n'''
    assert run_with_args("delete_interval 2021-05-03T12:00 2021-05-08T13:15") == b""
    assert run_with_args("delete_day 2021-05-04") == b""
    assert run_with_args(
        "delete_day 2021-05-03") == b"Can't delete booked interval: 2021-05-03 10:15:00\r\nCan't delete booked interval: 2021-05-03 10:30:00\r\n"
    assert run_with_args("delete_all") == b'All free slots removed\r\n'
