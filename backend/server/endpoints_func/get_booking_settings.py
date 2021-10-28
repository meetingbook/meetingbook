from db.models import BookingSettings, BookingSettingsSchema
from tools.for_db.work_with_admin_info import get_admin_id
from tools.build_response import build_response


def get_booking_settings(email_admin):
    try:
        id_admin = get_admin_id(email_admin)
        booking_settings = BookingSettings.query.with_entities(
            BookingSettings.start_time,
            BookingSettings.duration).filter(BookingSettings.admin_id == id_admin)
        slot_shema = BookingSettingsSchema(many=True)
        output = slot_shema.dump(booking_settings)
        return output
    except Exception as e:
        return build_response(e, 500)
