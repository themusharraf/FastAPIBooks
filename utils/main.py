from email.message import EmailMessage
from dotenv import load_dotenv
import smtplib
import os


def send_email(email: str | None, filename: str):
    load_dotenv()

    message = EmailMessage()
    message['from'] = os.getenv("FROM")
    message['to'] = email
    message['subject'] = "Web site register"

    # Read and set the HTML content as the main body
    with open(f"{filename}", 'r') as file:
        html_content = file.read()
    message.set_content("This is the plain text body of the email")
    message.add_alternative(html_content, subtype="html")

    # SMTP server configuration
    HOST = os.getenv("HOST")
    PORT = os.getenv("PORT")
    EMAIL = os.getenv("FROM")
    PASSWORD = os.getenv("PASS")

    # Send the email
    try:
        with smtplib.SMTP_SSL(HOST, PORT) as server:
            server.login(EMAIL, PASSWORD)
            server.send_message(message)
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")
