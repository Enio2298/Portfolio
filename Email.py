import smtplib
import os
from dotenv import load_dotenv

load_dotenv()


def send_email(message):
    try:
        # Setup SMTP server (Gmail example, adjust if using a different provider)
        smtp_server = "smtp.gmail.com"
        port = 587  # TLS port
        username = "enio2298@gmail.com"
        password = os.getenv("PASSWORD")
        receiver = "enio2298@gmail.com"

        # Email content
        subject = "Email from the portfolio"
        body = message
        message = f"Subject: {subject}\n\n{body}"

        # Establish connection and send email
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()  # Start TLS encryption
            server.login(username, password)  # Login to email account
            server.sendmail(username, receiver, message)  # Send email
    except Exception as e:
        print(f"Error: {e}")
