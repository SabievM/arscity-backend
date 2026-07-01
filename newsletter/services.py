
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from .models import Subscriber

from dotenv import load_dotenv
import os

load_dotenv()
ENVIRONMENT = os.environ.get("ENVIRONMENT", "development")

def send_products_email(products, mail_type):

    subscribers = Subscriber.objects.filter(
        is_active=True
    )

    template_map = {
        "new": "emails/new.html",
        "sale": "emails/sale.html",
        "collection": "emails/collection.html",
    }
    if ENVIRONMENT == "development":
        backend_base_url = "http://localhost:8000"
        frontend_base_url = "http://localhost:3000"
    else:
        backend_base_url = os.environ.get("BACKEND_BASE_URL")
        frontend_base_url = os.environ.get("FRONTEND_BASE_URL")

    template = template_map.get(mail_type)

    if products[0].get("type") == "showerassembly":
        catalog_products = "plumbing-fixtures"
    else:
        catalog_products = products[0].get("type")
    
    catalog_url = f"{frontend_base_url}/products/{catalog_products}"

    for subscriber in subscribers:

        unsubscribe_url = (
            f"{backend_base_url}/api/newsletter/unsubscribe/{subscriber.unsubscribe_token}/"
        )

        html = render_to_string(
            template,
            {
                "products": products,
                "unsubscribe_url": unsubscribe_url,
                "catalog_url": catalog_url,
                "catalog_products": catalog_products,
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


