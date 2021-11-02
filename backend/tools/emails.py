from flask_mail import Message
from tools.for_db.work_with_admin_info import get_admin_email_by_id


def send_email(admin_id, request_body, mail, link_id):
    email_admin = get_admin_email_by_id(admin_id)
    msg = Message('Hello, you have a new booking',
                  sender='booking@meetingbook.com',
                  recipients=[email_admin])
    body = '''Hey, {name} booked time: {start}-{end}. If you want to contact him: {email}. \
            Canel booking: http://localhost:5000/calendars/{link_id}/bookings/{booking_id} '''.format(
        name=request_body['guest_name'],
        start=request_body['start'],
        end=request_body['end'],
        email=request_body['guest_email'],
        link_id=link_id,
        booking_id=request_body['uuid'])
    msg.body = body if request_body['topic'] is None else '''{body}. User left a message for you: {topic}'''.format(
        body=body,
        topic=request_body['topic'])
    mail.send(msg)
