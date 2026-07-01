from newsletter.services import send_products_email


def send_newsletter_action(modeladmin, request, queryset, mail_type):
    """
    Универсальная рассылка
    """

    products = []

    for obj in queryset:

        image = ""
        type = obj.type.lower()
        id = obj.id

        if hasattr(obj, "image1") and obj.image1 and "grandfayans" not in obj.image1:
            image = obj.image1.url

        else:
            image = obj.image1.split("|")[0]
            
        products.append({
            "name": getattr(obj, "name", ""),
            "price": getattr(obj, "price", 0),
            "image": image,
            "type": type,
            "id": id
        })
    send_products_email(products, mail_type=mail_type)
    modeladmin.message_user(
        request,
        f"Рассылка '{mail_type}' отправлена ({len(products)} товаров)"
    )