"""
Mail server config
"""

from fastapi_mail import FastMail, ConnectionConfig, MessageSchema, MessageType
from pydantic import HttpUrl
from typing import Optional

from settings.config import CONFIG
import logging

mail_conf = ConnectionConfig(
    MAIL_USERNAME=CONFIG.mail_username,
    MAIL_PASSWORD=CONFIG.mail_password,
    MAIL_FROM=CONFIG.mail_sender,
    MAIL_PORT=CONFIG.mail_port,
    MAIL_SERVER=CONFIG.mail_server,
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True,
)

mail = FastMail(mail_conf)


async def send_signup_email(email: str):
    """Send user signup email"""

    if CONFIG.mail_console:
        print("Click Funnel Signup")
    else:
        message = MessageSchema(
            recipients=[email],
            subject="Click Funnel Signup",
            body=f"<p>Yooo thanks for signing up bruv.</p>",
            subtype=MessageType.html,
        )
        print("Click Funnel Signup Message")
        await mail.send_message(message)
