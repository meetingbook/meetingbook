import pytest

from cli.parser import regular_filter


@pytest.mark.parametrize("filter", [("free"),
                                    ("booking")])
def test_regular_filter_true(filter):
    assert regular_filter(filter) is True


@pytest.mark.parametrize("filter", [("123"),
                                    ("bear"),
                                    ("!@#$%^&*()_+?><,./")])
def test_regular_filter_false(filter):
    assert regular_filter(filter) is False
