import server as app


def test_response_post():
    with app.app.test_client() as con:
        resp = con.post('/schedule/start=2022-10-13T11:00&end=2022-15-14T13:00')
    assert resp.status_code == 200


def test_response_post_404():
    with app.app.test_client() as con:
        resp = con.post('/schedule/star=2022-10-13T11:00&end=2022-15-14T13:00')
    assert resp.status_code == 404
