import comand_line_parser
import pytest


@pytest.mark.parametrize("filter", [("free"),
                                    ("booking")])
def test_regular_filter_true(filter):
    assert comand_line_parser.regular_filter(filter) is True


@pytest.mark.parametrize("filter", [("123"),
                                    ("bear"),
                                    ("!@#$%^&*()_+?><,./")])
def test_regular_filter_false(filter):
    assert comand_line_parser.regular_filter(filter) is False
