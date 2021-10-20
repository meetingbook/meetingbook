from flask_mail import Message, Mail
from tools.for_db.work_with_admin_info import get_admin_email_by_id


def send_email(admin_id, start, end, guest_name, guest_email, topic):
    from server import app
    mail_req = Mail(app)
    email_admin = get_admin_email_by_id(admin_id)
    msg = Message('Hello, you have a new booking', sender='booking@meetingbook.com', recipients=[email_admin])
    body = '''Hey, {name} booked time: {start}-{end}. If you want to contact him: {email}.'''.format(
        name=guest_name, start=start, end=end, email=guest_email)
    if topic is None:
        msg.body = body
    else:
        msg.body = '''{body}. User left a message for you: {topic} '''.format(body=body, topic=topic)
    mail_req.send(msg)
