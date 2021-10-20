
from tools.unpack_json_booking_post import unpack_json_booking_post

json_with_topic = {'start': '2024-12-02T10:00:47.984Z',
                   'end': '2024-12-02T10:30:47.984Z',
                   'guest_name': 'Misha',
                   'guest_email': 'misha@gmail.com',
                   'topic': 'I want to discuss'
                   }

json_without_topic = {'start': '2024-12-02T10:00:47.984Z',
                      'end': '2024-12-02T10:30:47.984Z',
                      'guest_name': 'Misha',
                      'guest_email': 'misha@gmail.com',
                      }


def test_unpack_json_booking_post(app_for_test):
    start = unpack_json_booking_post(json_with_topic)
    start_1 = unpack_json_booking_post(json_without_topic)
    assert start[0] == '2024-12-02T10:00:47.984Z'
    assert start[1] == '2024-12-02T10:30:47.984Z'
    assert start[2] == 'Misha'
    assert start[3] == 'misha@gmail.com'
    assert start[4] == 'I want to discuss'
    assert start_1[0] == '2024-12-02T10:00:47.984Z'
    assert start_1[-1] is None
