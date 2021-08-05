import subprocess
import sys
import os


PYTHON_BINARY = sys.executable


def run_with_args(args):
    return subprocess.check_output(
        "{} cli/main.py -p db/test_main_db.sqlite {}".format(PYTHON_BINARY, args),
        shell=True)


def run_booking_with_args(args):
    return subprocess.check_output(
        "{} tests/test-tool.py {}".format(PYTHON_BINARY, args),
        shell=True)


def test_sanity():
    try:
        os.remove('db/test_main_db.sqlite')
    except FileNotFoundError:
        pass

    assert run_with_args("add_interval 2021-05-03T10:00 2021-05-10T11:15") == b""
    assert run_booking_with_args("2021-05-03T10:15 2021-05-03T11:00 testName test@test -t tteesstt") == b""
    assert run_with_args("get_slots -d 2021-05-03") == b"2021-05-03 10:00:00 - 2021-05-04 00:15:00\r\n"
    assert run_with_args("get_slots -d 2021-05-03 -f booking") == b"2021-05-03 10:15:00 - 2021-05-03 11:00:00\r\n"
    assert run_with_args(
        "get_slots -d 2021-05-03 -f free") == b'''2021-05-03 10:00:00 - 2021-05-03 10:15:00\r\n2021-05-03 11:00:00 -
        2021-05-04 00:15:00\r\n '''
    assert run_with_args("get_slots -w 2021-05-03") == b"2021-05-03 10:00:00 - 2021-05-10 00:15:00\r\n"
    assert run_with_args("get_slots -w 2021-05-03 -f booking") == b"2021-05-03 10:15:00 - 2021-05-03 11:00:00\r\n"
    assert run_with_args(
        "get_slots -w 2021-05-03 -f free") == b'''2021-05-03 10:00:00 - 2021-05-03 10:15:00\r\n2021-05-03 11:00:00 -
        2021-05-10 00:15:00\r\n '''
    assert run_with_args("delete_interval 2021-05-03T12:00 2021-05-08T13:15") == b""
    assert run_with_args("delete_day 2021-05-04") == b""
    assert run_with_args("delete_day 2021-05-03") == b"Can't delete booked interval: ('2021-05-03 07:15:00'," \
                                                     b")\r\nCan't delete booked interval: ('2021-05-03 07:30:00'," \
                                                     b")\r\nCan't delete booked interval: ('2021-05-03 07:45:00',)\r\n "
    assert run_with_args("delete_all") == b""
