from db.models import AdminInfo


def get_admin_id_by_email(email_admin):
    query_get_id_admin = AdminInfo.query.with_entities(AdminInfo.id).filter(AdminInfo.email == email_admin)
    return query_get_id_admin[0]["id"]
