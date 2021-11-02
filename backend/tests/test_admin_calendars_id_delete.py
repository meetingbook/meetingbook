from tools.for_db.work_with_links import add_link


def test_calendars_id_delete_200(app_for_test, test_admin, link_id):
    admin_id = test_admin.get_id()
    add_link(link_id, admin_id)
    response = app_for_test.delete(f'/calendars/{link_id}', headers=test_admin.get_valid_header())
    assert response.status == '200 OK'


def test_calendars_id_delete_404(app_for_test, test_admin):
    response = app_for_test.delete('/calendars/invalid_link', headers=test_admin.get_valid_header())
    assert response.status == '404 NOT FOUND'
    assert response.json == {'detail': 'Shareable link not found', 'status': 404}


def test_calendars_id_delete_401(app_for_test):
    response = app_for_test.delete('/calendars/invalid_link')
    assert response.status == '401 UNAUTHORIZED'
