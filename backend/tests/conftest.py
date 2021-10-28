import pytest
from tools.for_test.create_db_for_tests import AdminForTests, create_test_app_with_db


@pytest.fixture(scope='session')
def test_admin():
    admin = AdminForTests()
    yield admin


@pytest.fixture(scope='session')
def link_id():
    yield 'link_id'


@pytest.fixture(scope='module')
def app_for_test():
    yield create_test_app_with_db().test_client()
