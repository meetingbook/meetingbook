from flask_mail import Message, Mail
from tools.for_db.work_with_admin_info import get_admin_email_by_id


def send_email(admin_id, request_body):
    from server import app
    mail_req = Mail(app)
    email_admin = get_admin_email_by_id(admin_id)
    msg = Message('Hello, you have a new booking',
                  sender='booking@meetingbook.com',
                  recipients=[email_admin])
    body = '''Hey, {name} booked time: {start}-{end}. If you want to contact him: {email}.'''.format(
        name=request_body['guest_name'],
        start=request_body['start'],
        end=request_body['end'],
        email=request_body['guest_email'])
    msg.body = body if request_body['topic'] is None else '''{body}. User left a message for you: {topic}'''.format(
        body=body,
        topic=request_body['topic'])
    mail_req.send(msg)
