# from django.conf import settings
# from django.template.loader import render_to_string
# from django.core.mail import EmailMultiAlternatives
# from .models import Subscriber


# def send_products_email(products, mail_type):

#     recipients = Subscriber.objects.values_list("email", flat=True)

#     # выбираем шаблон
#     template_map = {
#         "new": "emails/new.html",
#         "sale": "emails/sale.html",
#         "collection": "emails/collection.html",
#     }

#     template = template_map.get(mail_type, template_map[mail_type])

#     html = render_to_string(template, {
#         "products": products
#     })

#     for email in recipients:

#         msg = EmailMultiAlternatives(
#             subject="ARS City",
#             body="HTML письмо",
#             from_email=settings.DEFAULT_FROM_EMAIL,
#             to=[email]
#         )

#         msg.attach_alternative(html, "text/html")
#         msg.send()
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from .models import Subscriber


def send_products_email(products, mail_type):

    subscribers = Subscriber.objects.filter(
        is_active=True
    )

    template_map = {
        "new": "emails/new.html",
        "sale": "emails/sale.html",
        "collection": "emails/collection.html",
    }

    template = template_map.get(mail_type)

    for subscriber in subscribers:

        unsubscribe_url = (
            f"http://localhost:8000/api/newsletter/unsubscribe/{subscriber.unsubscribe_token}/"
        )

        html = render_to_string(
            template,
            {
                "products": products,
                "unsubscribe_url": unsubscribe_url,
            }
        )

        msg = EmailMultiAlternatives(
            subject="ARS City",
            body="HTML письмо",
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[subscriber.email]
        )

        msg.attach_alternative(html, "text/html")
        msg.send()