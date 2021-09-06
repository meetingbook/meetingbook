#!/usr/bin/env python3

import argparse
from cli.db import delete_all as da, delete_day as dd, add_interval as ai, delete_interval as di, get_slots
import re


def createParser():
    """создает парсер,подпарсер с аргументами командной строки"""
    parser = argparse.ArgumentParser(
        description="reads commands and arguments",
        prog="calendar")
    parser.add_argument('--path', '-p', default='db/main_db.sqlite',
                        help="the path to the database. Default: main_db.sqlite")
    subparsers = parser.add_subparsers(dest='command',
                                       title="Used commands",
                                       description='Commands to be taken as the first parameter %(prog)s')

    add_interval = subparsers.add_parser('add_interval')
    add_interval.add_argument('start', help="start of added interval: YYYY-MM-DDThh:mm")
    add_interval.add_argument('end', help="end of added interval: YYYY-MM-DDThh:mm")

    delete_interval = subparsers.add_parser('delete_interval')
    delete_interval.add_argument('start', help="start of the deleted interval: YYYY-MM-DDThh:mm")
    delete_interval.add_argument('end', help="end of interval to delete: YYYY-MM-DDThh:mm")

    delete_day = subparsers.add_parser('delete_day')
    delete_day.add_argument('date', help="deleted day: YYYY-MM-DD")

    get_slots = subparsers.add_parser('get_slots')
    get_slots.add_argument('--week', '-w', help="interval of seven days from the specified: YYYY-MM-DD")
    get_slots.add_argument('--day', '-d', help="interval of the specified day: YYYY-MM-DD")
    get_slots.add_argument(
        '--filter', '-f', help="booking and free intervals", choices=['booking', 'free'])

    subparsers.add_parser('delete_all')
    return parser


def correctness_commands(params):
    """проверяет на правильность команд"""

    if params.command == "add_interval":
        check_format_add_and_del_interval(params, ai.add_interval)
    elif params.command == "delete_interval":
        check_format_add_and_del_interval(params, di.delete_interval)
    elif params.command == "delete_day":
        check_format_delete_day(params)
    elif params.command == "get_slots":
        check_format_get_slots(params)
    elif params.command == "delete_all":
        da.delete_all(params)

    else:
        print("""Input command!:
        ./main.py [-p][--path] <command> <arguments>
        Command:           Arguments:           Format:
         add_interval       start end        ->  YYYY-MM-DDThh:mm  YYYY-MM-DDThh:mm
         delete_interval    start end        ->  YYYY-MM-DDThh:mm  YYYY-MM-DDThh:mm
         delete_day         date             ->  YYYY-MM-DD
         get_slots          [-w] [-d] [-f]   ->  week & day: YYYY-MM-DD,
                                                 filter: 'free' or 'booking'.
         delete_all         no args          ->  delete all free slots
        """)


def check_format_add_and_del_interval(params, func):
    """запуск функции add_interval и delete_interval если аргументы соответствуют условию"""
    if (regular_start_end(params.start) is True) and (regular_start_end(params.end) is True):
        func(params)
    else:
        print("assert: YYYY-MM-DDThh:mm")


def check_format_delete_day(params):
    """запуск функции delete_day, если аргументы соответствуют условию"""
    if regular_day(params.date) is True:
        dd.delete_day(params)
    else:
        print("assert: YYYY-MM-DD")


def check_format_get_slots(params):
    """запуск функции get_slots, если аргументы соответствуют условию"""
    if (check_day_and_week(params.week) is False) or (check_day_and_week(params.day) is False) or (
            check_filter(params) is False):
        print("assert: YYYY-MM-DD")
    else:
        get_slots.get_slots(params)


def check_day_and_week(params):
    """проверка что day не равен None"""
    if params is not None:
        return regular_day(params)
    else:
        return True


def check_filter(params):
    """проверка что filter не равен None"""
    if params.filter is not None:
        return regular_filter(params.filter)
    else:
        return True


def regular_filter(x):
    """проверка соответствия filter одному из двух значений[booking,free]"""
    if (x == "booking") or (x == "free"):
        return True
    else:
        return False


def regular_start_end(x):
    """регулярка для проверки формата start и end[YYYY-MM-DDThh:mm]"""
    pattern = r'^([0-9]{4}[-]?((0[13-9]|1[012])[-]?(0[1-9]|[12][0-9]|30)|(0[13578]|1[02])[-]?31|02[-]?(0[1-9]|1[0-9]|2[0-8]))|([0-9]{2}(([2468][048]|[02468][48])|[13579][26])|([13579][26]|[02468][048])00)[-]?02[-]?29)[T](0[0-9]|1[0-9]|2[0-3])[:]([0-5]{1}[0-9]{1})$'  # noqa: E501

    if re.match(pattern, x):
        return True
    else:
        print('wrong format {}'.format(x))
        return False


def regular_day(x):
    """регулярка для проверки формата date[YYYY-MM-DD]"""
    pattern = r'^([0-9]{4}[-]?((0[13-9]|1[012])[-]?(0[1-9]|[12][0-9]|30)|(0[13578]|1[02])[-]?31|02[-]?(0[1-9]|1[0-9]|2[0-8]))|([0-9]{2}(([2468][048]|[02468][48])|[13579][26])|([13579][26]|[02468][048])00)[-]?02[-]?29)$'  # noqa: E501

    if re.match(pattern, x):
        return True
    else:
        print('wrong format {}'.format(x))
        return False
