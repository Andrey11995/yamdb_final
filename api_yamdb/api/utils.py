import uuid

from django.core.mail import EmailMessage


def send_email(username, email, code):
    """Метод отправки письма с кодом подтверждения на почту."""
    email_body = (f'Привет {username}, твой код '
                  f'подтверждения: {code}!')
    email = EmailMessage(
        subject='Код подтверждения',
        body=email_body,
        to=[email]
    )
    email.send()


def code_gen():
    """Генератор кода подтверждения."""
    return str(uuid.uuid4()).split('-')[0]
