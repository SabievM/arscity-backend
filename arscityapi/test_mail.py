# test_mail.py
from django.core.mail import send_mail

send_mail(
    subject="Тест",
    message="Проверка отправки",
    from_email=None,
    recipient_list=["msabieff@yandex.ru"],
)