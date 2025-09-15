import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# SMTP
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 465
SMTP_USERNAME = 'nyameget@gmail.com'
SMTP_PASSWORD = 'xozhynlsirmromlx'
EMAIL_SENDER = 'nyameget@gmail.com'

# Multiple recipients
RECIPIENTS = [
    "desmondeshun134@gmail.com",
    "nyameget@gmail.com",
    "isaac4230220@gmail.com"
]


def generate_booking_email(booking):
    customer_name = booking.name
    customer_email = booking.email
    customer_phone = booking.phone
    destination = booking.destination
    travel_date = booking.travel_date
    special_requests = booking.special_note

    # Subject
    subject = f"New Booking: {destination} – {customer_name}"

    # Plain text body
    body = f"""
Hello Guide,

A new booking has been made. Please find the details below:

- Full Name: {customer_name}
- Email: {customer_email}
- Phone: {customer_phone}
- Destination: {destination}
- Date of Travel: {travel_date}
- Special Requests: {special_requests if special_requests else "None"}

Please prepare accordingly and reach out to the customer if needed.

Thank you,
GlobeTrek Travel Agency
    """

    # Create MIMEText message
    msg = MIMEMultipart()
    msg["Subject"] = subject
    msg["From"] = EMAIL_SENDER
    msg["To"] = ", ".join(RECIPIENTS)  # show all in email header

    msg.attach(MIMEText(body, "plain"))

    return msg


def send_email_smtp(new_booking):
    """Send email via SMTP."""
    try:
        msg = generate_booking_email(new_booking)
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.sendmail(EMAIL_SENDER, RECIPIENTS, msg.as_string())
            print(f"Email sent to {', '.join(RECIPIENTS)}")

    except Exception as e:
        print(f"Email sending failed: {e}")
        raise
