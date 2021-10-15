from datetime import datetime
from datetime import date

ISO8601 = '%Y-%m-%dT%H:%M:%S%z'


def str_to_iso8601(input: str) -> date:
    return datetime.strptime(input, ISO8601)


def iso8601_to_str(input: date) -> str:
    return input.strftime(ISO8601)
