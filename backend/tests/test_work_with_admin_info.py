from db import models
from tools.for_db.work_with_admin_info import add_admin, get_admin_email_by_id, get_admin_id, get_psw_from_db


def test_get_psw_from_db(app_for_test):
    admin = models.AdminInfo(email='correct@email.com', psw='qwertyuiop')
    models.db.session.add(admin)
    models.db.session.commit()
    assert get_psw_from_db('correct@email.com') == 'qwertyuiop'


def test_add_admin(app_for_test):
    admin_before = models.AdminInfoShema(many=True).dump(models.AdminInfo.query.all())
    add_admin("newadmin@gmail.com", 'newpassword')
    admin_after = models.AdminInfoShema(many=True).dump(models.AdminInfo.query.all())
    assert admin_before == [{'email': 'correct@email.com', 'id': 1, 'psw': 'qwertyuiop', 'slots': []}]
    assert admin_after == [{'email': 'correct@email.com', 'id': 1, 'psw': 'qwertyuiop', 'slots': []},
                           {'email': 'newadmin@gmail.com', 'id': 2, 'psw': 'newpassword', 'slots': []}]


def test_get_admin_id(app_for_test):
    assert get_admin_id('newadmin@gmail.com') == 2


def test_get_admin_email(app_for_test):
    assert get_admin_email_by_id(1) == 'correct@email.com'
