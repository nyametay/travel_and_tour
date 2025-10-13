import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv

load_dotenv()

# Load from environment variables
SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
EMAIL_SENDER = os.getenv('EMAIL_SENDER') # verified sender in SendGrid
RECIPIENTS = [
    "desmondeshun134@gmail.com",
    "guide2@example.com",
    "guide3@example.com"
]


def generate_booking_email(booking):
    """Generate the email content for the booking."""
    customer_name = booking.name
    customer_email = booking.email
    customer_phone = booking.phone
    destination = booking.destination
    travel_date = booking.travel_date
    special_requests = booking.special_note

    subject = f"New Booking: {destination} – {customer_name}"

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

    return subject, body


def send_email_sendgrid(new_booking):
    """Send booking email via SendGrid API."""
    try:
        subject, body = generate_booking_email(new_booking)

        message = Mail(
            from_email=EMAIL_SENDER,
            to_emails=RECIPIENTS,
            subject=subject,
            plain_text_content=body,
        )

        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)

        print(f"✅ Email sent to {', '.join(RECIPIENTS)} (Status: {response.status_code})")

    except Exception as e:
        print(f"❌ Email sending failed: {e}")
        raise
