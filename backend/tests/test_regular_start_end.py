import comand_line_parser
import pytest


@pytest.mark.parametrize("date", [("2021-01-02T11:00"),
                                  ("2020-10-15T09:15")])
def test_regular_start_end_positive(date):
    assert comand_line_parser.regular_start_end(date) is True


@pytest.mark.parametrize("date", [("2021-13-02T11:00"),
                                  ("2021-01-32T11:00"),
                                  ("2021-01-02T25:00"),
                                  ("2021-01-02T11:60"),
                                  ("2021-01-02T11:0"),
                                  ("2021-02-30T11:00")])
def test_regular_start_end_negative(date):
    assert comand_line_parser.regular_start_end(date) is False
