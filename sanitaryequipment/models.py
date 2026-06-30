from django.db import models

class ShowerAssembly(models.Model):
    """
    Модель товара (сантехника / мебель) с атрибутами из прайс-листа.
    """

    # Идентификатор и основные поля
    article = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Артикул",
        help_text="Уникальный артикул товара"
    )
    name = models.CharField(
        max_length=255,
        verbose_name="Название товара"
    )
    price = models.CharField(
        verbose_name="Цена (РРЦ)",
        help_text="Рекомендуемая розничная цена"
    )
    category = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name="Категория"
    )


    # Медиа и ссылки
    photos = models.CharField(
        blank=True,
        null=True,
        verbose_name="Фотографии",
    )
    image1 = models.URLField(
        blank=True,
        null=True,
        verbose_name="Изображение 1",
    )
    link = models.URLField(
        max_length=500,
        blank=True,
        null=True,
        verbose_name="Ссылка на товар"
    )

    # Количественные показатели
    stock = models.CharField(
        blank=True,
        null=True,
        verbose_name="Остатки"
    )
    manufacturer = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name="Производитель"
    )
    product_type = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name="Вид изделия"
    )

    # Цвета и материалы
    profile_color = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Цвет профиля"
    )
    material = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name="Материал"
    )
    facade_material = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name="Материал фасада"
    )
    body_material = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name="Материал корпуса"
    )
    main_material = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name="Основной материал"
    )
    product_color = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Цвет изделия"
    )
    body_coating = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name="Покрытие корпуса"
    )

    # Булевы характеристики
    has_shelf = models.CharField(
        verbose_name="Наличие полки"
    )
    rimless = models.CharField(
        verbose_name="Безободковый"
    )
    seat_lift  = models.CharField(
        verbose_name="Микролифт на сиденье"
    )
    armrest  = models.CharField(
        verbose_name="Наличие подлокотника"
    )
    has_drawers = models.CharField(
        verbose_name="Наличие ящиков"
    )
    door_closers  = models.CharField(
        verbose_name="Доводчики дверей"
    )
    drawer_closers  = models.CharField(
        verbose_name="Доводчики ящика"
    )
    built_in_bidet  = models.CharField(
        verbose_name="Встроенное биде"
    )
    seat_included = models.CharField(
        verbose_name="Сиденье в комплекте"
    )
    anti_splash = models.CharField(
        verbose_name="Система антивсплекс"
    )

    # Строковые поля с выбором / типом
    flush_type = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Тип смыва"
    )
    discharge_type = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Тип выпуска"
    )
    flush_mode = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Режим смыва воды"
    )
    seat_material = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Материал сиденья"
    )
    style = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Стиль"
    )
    sink_type = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Тип мойки"
    )
    washbasin_type = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Тип раковины"
    )
    mounting_type = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Тип монтажа"
    )
    collection = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name="Коллекция набора"
    )
    warranty = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Гарантия"
    )
    brand = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name="Марка (Бренд)"
    )

    # Числовые размеры и объёмы
    depth = models.CharField(
        blank=True,
        null=True,
        verbose_name="Глубина"
    )
    volume = models.CharField(
        blank=True,
        null=True,
        verbose_name="Объем"
    )
    drawers_count  = models.CharField(
        blank=True,
        null=True,
        verbose_name="Количество ящиков"
    )
    tank_volume = models.CharField(
        blank=True,
        null=True,
        verbose_name="Объем бака в литрах"
    )
    dimensions_length  = models.CharField(
        blank=True,
        null=True,
        verbose_name="Габариты длина, мм"
    )
    dimensions_width = models.CharField(
        blank=True,
        null=True,
        verbose_name="Габариты ширина, мм"
    )
    dimensions_height = models.CharField(
        blank=True,
        null=True,
        verbose_name="Габариты высота, мм"
    )
    type= models.CharField(max_length=255, default="ShowerAssembly")

    # Системные поля
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата обновления"
    )

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ['name']

    def __str__(self):
        return f"{self.article} - {self.name}"