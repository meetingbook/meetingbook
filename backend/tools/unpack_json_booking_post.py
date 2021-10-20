

def unpack_json_booking_post(request_body):
    return request_body['start'], request_body['end'], request_body['guest_name'], request_body['guest_email'],\
        request_body['topic'] if 'topic' in request_body else None
