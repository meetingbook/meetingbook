import pytest
from db.models import db
from tools.datetime_convertations import DateTime
from tools.for_db.work_with_slots import add_slot_and_get_id, get_slot_by_id, get_id_slice_of_slot, query_slots, \
    marshmallow_for_query_slots, DbSlotException, update_booking_id_in_slot, canceling_booking_id_from_slot

start = DateTime().utc_plus_delta(hours=1)
end = DateTime().utc_plus_delta(hours=10)
start_slice = DateTime().utc_plus_delta(hours=3)
end_slice = DateTime().utc_plus_delta(hours=5)


def test_add_slot(test_admin):
    slot_id = add_slot_and_get_id(start, end, test_admin.get_id())
    assert get_slot_by_id(slot_id) == {'id': 1, 'start_interval': start, 'end_interval': end, 'booking_id': None}
    with pytest.raises(DbSlotException):
        add_slot_and_get_id(start, end, test_admin.get_id())


def test_get_id_slice_of_slot(test_admin):
    slice_id = get_id_slice_of_slot(start_slice, end_slice, test_admin.get_id())
    assert get_slot_by_id(slice_id) == {'id': slice_id, 'start_interval': start_slice, 'end_interval': end_slice,
                                        'booking_id': None}
    slots = query_slots(test_admin.get_id(), start, end)
    assert marshmallow_for_query_slots(slots) == [{'booking_id': None,
                                                   'end_interval': start_slice,
                                                   'id': slice_id-2,
                                                   'start_interval': start},
                                                  {'booking_id': None,
                                                   'end_interval': end,
                                                   'id': slice_id-1,
                                                   'start_interval': end_slice},
                                                  {'booking_id': None,
                                                   'end_interval': end_slice,
                                                   'id': slice_id,
                                                   'start_interval': start_slice}]


def test_update_booking_id_in_slot(test_admin):
    update_booking_id_in_slot(4, 1)
    assert get_slot_by_id(4) == {'id': 4, 'start_interval': start_slice, 'end_interval': end_slice, 'booking_id': 1}
    with pytest.raises(DbSlotException):
        get_id_slice_of_slot(start_slice, end_slice, test_admin.get_id())


def test_canceling_booking_id_from_slot(test_admin):
    try:
        canceling_booking_id_from_slot(1)
        db.session.commit()
    except DbSlotException:
        db.session.rollback()
        raise
    finally:
        db.session.close()
    assert get_slot_by_id(4) == {'id': 4, 'start_interval': start_slice, 'end_interval': end_slice, 'booking_id': None}
