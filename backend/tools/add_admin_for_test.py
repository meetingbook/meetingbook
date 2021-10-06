import base64
from tools.func_for_psw import password_hashing
import db.models as models

valid_credentials = base64.b64encode(b'test@test.test:testtest').decode('utf-8')


def add_admin_for_test(email, psw):
    hash_psw = password_hashing(psw)
    admin = models.AdminInfo(email=email, psw=hash_psw)
    models.db.session.add(admin)
    models.db.session.commit()
