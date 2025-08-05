import smtplib
from email.message import EmailMessage

# Fixed sender credentials
SENDER_EMAIL = "sp9872239@gmail.com"
SENDER_PASSWORD = "psul tjpb wxbh qgjf"

def send_html_email(subject, html_content, to_email):
    """
    Send an HTML email via Gmail SMTP.

    Parameters:
    - html_content (str): HTML content of the email page design
    - to_email (str): Recipient email address
    """

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = SENDER_EMAIL
    msg['To'] = to_email

    # Set both plain text and HTML (optional plain text for fallback)
    msg.set_content("This email contains HTML content. Please use an HTML-capable client.")
    msg.add_alternative(html_content, subtype='html')

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
            smtp.send_message(msg)
        print("Email sent successfully.")
    except Exception as e:
        print("Failed to send HTML email:", e)
