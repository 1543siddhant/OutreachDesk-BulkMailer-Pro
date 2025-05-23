import os
import smtplib
import time
from email.message import EmailMessage

# === CONFIGURATION ===
SENDER_EMAIL = "siddhantpatil1543@gmail.com"
SENDER_PASSWORD = "ijkznkrieizwqznd"   # <-- your App Password
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

RECIPIENTS_FILE = "emails.txt"   # one email address per line
RESUME_PATH = r"D:\Bulk Email sender\OutreachDesk-BulkMailer-Pro\Siddhant Dinesh Patil Resume4.pdf"

SUBJECT = "Your Fixed Subject Here"
BODY = """\
Dear Recipient,

Hello World
Best regards,
Siddhant Patil
"""

# === READ RECIPIENTS ===
with open(RECIPIENTS_FILE, "r") as f:
    recipients = [line.strip() for line in f if line.strip()]

# === LOAD RESUME ONCE ===
with open(RESUME_PATH, "rb") as f:
    resume_data = f.read()
resume_filename = os.path.basename(RESUME_PATH)

# === SEND EMAIL FUNCTION ===
def send_email(to_address):
    msg = EmailMessage()
    msg["From"] = SENDER_EMAIL
    msg["To"] = to_address
    msg["Subject"] = SUBJECT
    msg.set_content(BODY)

    # Attach resume
    msg.add_attachment(
        resume_data,
        maintype="application",
        subtype="pdf",
        filename=resume_filename
    )

    # Send via Gmail SMTP server
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
        smtp.send_message(msg)

# === MAIN ===
if __name__ == "__main__":
    for idx, recipient in enumerate(recipients, start=1):
        try:
            send_email(recipient)
            print(f"[{idx}/{len(recipients)}] ✅ Sent to {recipient}")
        except Exception as e:
            print(f"[{idx}/{len(recipients)}] ❌ Failed to {recipient}: {e}")
        time.sleep(1)   # slight pause to avoid rate-limits
