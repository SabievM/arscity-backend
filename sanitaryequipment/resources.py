from import_export import resources, fields
from import_export.widgets import CharWidget
from .models import ShowerAssembly



class ProductResource(resources.ModelResource):
    # ... существующие поля ...
    article = fields.Field(column_name='Артикул', attribute='article', widget=CharWidget())
    name = fields.Field(column_name='Название товара', attribute='name', widget=CharWidget())
    price = fields.Field(column_name='Цена (РРЦ)', attribute='price', widget=CharWidget())
    category = fields.Field(column_name='Категория', attribute='category', widget=CharWidget())
    photos = fields.Field(column_name='Фотографии', attribute='photos', widget=CharWidget())
    image1 = fields.Field(column_name='Фотографии', attribute='image1', widget=CharWidget())
    link = fields.Field(column_name='Ссылка', attribute='link', widget=CharWidget())
    stock = fields.Field(column_name='Остатки', attribute='stock', widget=CharWidget())
    manufacturer = fields.Field(column_name='Производитель', attribute='manufacturer', widget=CharWidget())
    product_type = fields.Field(column_name='Вид изделия', attribute='product_type', widget=CharWidget())
    profile_color = fields.Field(column_name='Цвет профиля', attribute='profile_color', widget=CharWidget())
    has_shelf = fields.Field(column_name='Наличие полки', attribute='has_shelf', widget=CharWidget())
    flush_type = fields.Field(column_name='Тип смыва', attribute='flush_type', widget=CharWidget())
    rimless = fields.Field(column_name='Безободковый', attribute='rimless', widget=CharWidget())
    discharge_type = fields.Field(column_name='Тип выпуска', attribute='discharge_type', widget=CharWidget())
    flush_mode = fields.Field(column_name='Режим смыва воды', attribute='flush_mode', widget=CharWidget())
    seat_material = fields.Field(column_name='Материал сиденья', attribute='seat_material', widget=CharWidget())

    # --- ДОБАВЛЕННЫЕ ПОЛЯ (продолжение) ---
    seat_lift = fields.Field(
        column_name='Микролифт на сиденье',
        attribute='seat_lift',
        widget=CharWidget()
    )
    material = fields.Field(
        column_name='Материал',
        attribute='material',
        widget=CharWidget()
    )
    depth = fields.Field(
        column_name='Глубина',
        attribute='depth',
        widget=CharWidget()
    )
    volume = fields.Field(
        column_name='Объем',
        attribute='volume',
        widget=CharWidget()
    )
    armrest = fields.Field(
        column_name='Наличие подлокотника',
        attribute='armrest',
        widget=CharWidget()
    )
    style = fields.Field(
        column_name='Стиль',
        attribute='style',
        widget=CharWidget()
    )
    facade_material = fields.Field(
        column_name='Материал фасада',
        attribute='facade_material',
        widget=CharWidget()
    )
    body_material = fields.Field(
        column_name='Материал корпуса',
        attribute='body_material',
        widget=CharWidget()
    )
    has_drawers = fields.Field(
        column_name='Наличие ящиков',
        attribute='has_drawers',
        widget=CharWidget()
    )
    body_coating = fields.Field(
        column_name='Покрытие корпуса',
        attribute='body_coating',
        widget=CharWidget()
    )
    drawers_count = fields.Field(
        column_name='Количество ящиков',
        attribute='drawers_count',
        widget=CharWidget()
    )
    door_closers = fields.Field(
        column_name='Доводчики дверей',
        attribute='door_closers',
        widget=CharWidget()
    )
    drawer_closers = fields.Field(
        column_name='Доводчики ящика',
        attribute='drawer_closers',
        widget=CharWidget()
    )
    sink_type = fields.Field(
        column_name='Тип мойки',
        attribute='sink_type',
        widget=CharWidget()
    )
    product_color = fields.Field(
        column_name='Цвет изделия',
        attribute='product_color',
        widget=CharWidget()
    )
    built_in_bidet = fields.Field(
        column_name='Встроенное биде',
        attribute='built_in_bidet',
        widget=CharWidget()
    )
    tank_volume = fields.Field(
        column_name='Объем бака в литрах',
        attribute='tank_volume',
        widget=CharWidget()
    )
    seat_included = fields.Field(
        column_name='Сиденье в комплекте',
        attribute='seat_included',
        widget=CharWidget()
    )
    anti_splash = fields.Field(
        column_name='Система антивсплекс',
        attribute='anti_splash',
        widget=CharWidget()
    )
    washbasin_type = fields.Field(
        column_name='Тип раковины',
        attribute='washbasin_type',
        widget=CharWidget()
    )
    main_material = fields.Field(
        column_name='Основной материал',
        attribute='main_material',
        widget=CharWidget()
    )
    dimensions_length = fields.Field(
        column_name='Габариты длина, мм',
        attribute='dimensions_length',
        widget=CharWidget()
    )
    dimensions_width = fields.Field(
        column_name='Габариты ширина, мм',
        attribute='dimensions_width',
        widget=CharWidget()
    )
    dimensions_height = fields.Field(
        column_name='Габариты высота, мм',
        attribute='dimensions_height',
        widget=CharWidget()
    )
    collection = fields.Field(
        column_name='Коллекция набора',
        attribute='collection',
        widget=CharWidget()
    )
    warranty = fields.Field(
        column_name='Гарантия',
        attribute='warranty',
        widget=CharWidget()
    )
    mounting_type = fields.Field(
        column_name='Тип монтажа',
        attribute='mounting_type',
        widget=CharWidget()
    )
    brand = fields.Field(
        column_name='Марка (Бренд)',
        attribute='brand',
        widget=CharWidget()
    )
    

    class Meta:
        model = ShowerAssembly
        fields = (
            'article', 'name', 'price', 'category', 'photos', 'image1', 'link', 'stock',
            'manufacturer', 'product_type', 'profile_color', 'has_shelf',
            'flush_type','rimless', 'discharge_type','flush_mode', 'seat_material',
            # добавленные поля
            'seat_lift', 'material', 'depth', 'volume', 'armrest', 'style',
            'facade_material', 'body_material', 'has_drawers', 'body_coating',
            'drawers_count', 'door_closers', 'drawer_closers', 'sink_type',
            'product_color', 'built_in_bidet', 'tank_volume', 'seat_included',
            'anti_splash', 'washbasin_type', 'main_material', 'dimensions_length',
            'dimensions_width', 'dimensions_height', 'collection', 'warranty',
            'mounting_type', 'brand',
        )
        import_id_fields = ('article',)
        skip_unchanged = False
        report_skipped = True
    def before_import_row(self, row, **kwargs):
        category = row.get("Категория")

        if category and "|" in category:
            parts = category.split("|")
            if len(parts) > 1:
                row["Категория"] = parts[1]

                