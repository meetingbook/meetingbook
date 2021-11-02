from tools.datetime_convertations import DateTime
from tools.for_db.work_with_links import add_link, query_links, delete_link, get_link

valid_until = DateTime().utc_plus_delta(days=7)


def test_links_add(app_for_test, test_admin, link_id):
    admin_id = test_admin.get_id()
    add_link(link_id, admin_id, valid_until)
    add_link('second_link_id', admin_id, valid_until)
    assert query_links(admin_id) == [{'id': 1, 'link_id': 'link_id', 'valid_until': valid_until},
                                     {'id': 2, 'link_id': 'second_link_id', 'valid_until': valid_until}]
    assert get_link(link_id).admin_id == admin_id


def test_links_delete(app_for_test, link_id):
    admin_id = get_link(link_id).admin_id
    delete_link(admin_id, link_id)
    assert query_links(admin_id) == [{'id': 2, 'link_id': 'second_link_id', 'valid_until': valid_until}]
