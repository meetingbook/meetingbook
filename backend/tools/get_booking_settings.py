from db.models import BookingSettings, BookingSettingsSchema, AdminInfo


def get_booking_settings(email_admin):
    try:
        query_get_id_admin = AdminInfo.query.with_entities(AdminInfo.id).filter(AdminInfo.email == email_admin)
        id_admin = query_get_id_admin[0]["id"]
        booking_settings = BookingSettings.query.with_entities(
            BookingSettings.start_time,
            BookingSettings.duration).filter(BookingSettings.admin_id == id_admin)
        slot_shema = BookingSettingsSchema(many=True)
        output = slot_shema.dump(booking_settings)
        return output
    except Exception as e:
        return {'detail': f'{e}', 'status': 500}
