import pytest
from tools.create_db_for_tests import AdminForTests


@pytest.fixture(scope='session')
def test_admin():
    admin = AdminForTests()
    yield admin


@pytest.fixture(scope='session')
def link_id():
    yield 'link_id'
