from db.models import Slots, SlotsShema
from datetime import timedelta
from tools.transform_str_to_datetime_and_back import transform_string_to_datetime, transform_datetime_to_string


def get_slots_in_week(date):
    """Return list of slots for the week starting from <date>
    """
    end_interval = transform_datetime_to_string(transform_string_to_datetime(date) + timedelta(days=7))

    list_of_slots_in_week = Slots.query.filter(Slots.start_interval.between(date, end_interval)).all()
    slots_shema = SlotsShema(many=True)
    output = slots_shema.dump(list_of_slots_in_week)
    return output
