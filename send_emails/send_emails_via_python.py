import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders

SMTP_SERVER = 'smtp.gmail.com'
PORT = 587
SENDER_EMAIL = "abc@gmail.com"
SENDER_PASSWORD = "<your_app_password>"
RECIPIENT_EMAIL = "xyz@gmail.com"
subject = "RFM Analysis: Identify Valuable Customers."
body = """
  RFM analysis is a marketing technique that uses customer behavior data to identify and target the most valuable customers. RFM stands for recency, frequency, and monetary value.
  This analysis will impact Customer Retention, Product sales, and marketing too.
  Often times a customer might have bought a high-valued/priced item and then after that, he might have not purchased anything and he might become the highest sales-valued customer.
  RFM Analysis solves this issue by taking multiple factors into consideration
  Definition: RFM (Recency, Frequency, and Monetary) analysis is the most simple and proven technique used by marketing people for customer segmentation.
  1. How recently (Recency).
  2. How often (Frequency).
  3. How much did they buy (Monetary)?
"""

def send_email(sender_email, sender_password, recipient_email, subject, body, attachment_path=None):
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = subject

    message.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP(SMTP_SERVER, PORT) as server:
            server.starttls()  # Enable security
            server.login(sender_email, sender_password)  # Log in to the server
            text = message.as_string()
            server.sendmail(sender_email, recipient_email, text)  # Send email
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

send_email(
    sender_email=SENDER_EMAIL,
    sender_password=SENDER_PASSWORD,
    recipient_email=RECIPIENT_EMAIL,
    subject=subject,
    body=body,
)