import comand_line_parser
import pytest


@pytest.mark.parametrize("date", [("2021-01-02"),
                                  ("2020-10-15")])
def test_regular_day_positive(date):
    assert comand_line_parser.regular_day(date) is True


@pytest.mark.parametrize("date", [("2021-13-02"),
                                  ("2021-01-32"),
                                  ("2021-01-0"),
                                  ("2021-02-30")])
def test_regular_day_negative(date):
    assert comand_line_parser.regular_day(date) is False
