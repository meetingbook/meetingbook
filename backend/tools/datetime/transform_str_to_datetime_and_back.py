from datetime import datetime


def transform_string_to_datetime(date):
    date = datetime.fromisoformat(date)  # transform string to datetime object
    return date


def transform_datetime_to_string(datetime):
    return datetime.strftime("%Y-%m-%d")  # transform datetime object to string
