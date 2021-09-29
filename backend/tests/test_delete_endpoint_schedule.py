import server as app


def test_response_delete():
    with app.app.test_client() as con:
        resp = con.delete('/schedule/interval_id=1')
    assert resp.status_code == 200
