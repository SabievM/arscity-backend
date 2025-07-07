from django.db import models


class Category(models.Model):
    name = models.CharField("Название категории", max_length=255)

    class Meta:
        verbose_name = 'Название категории'
        verbose_name_plural = 'Категория'

    def __str__(self): 
        return self.name



class Country(models.Model):
    name = models.CharField("Страна", max_length=100)

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страна'

    def __str__(self): 
        return self.name

class Collection(models.Model):
    name = models.CharField("Название коллекции", max_length=255)
    scope_of_application = models.CharField("Область применения", max_length=255, blank=True, null=True)
    main_size = models.CharField('Основной размер', max_length=255, blank=True, null=True)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2, default=0)
    colors = models.CharField('Цвета', max_length=255, blank=True, null=True)
    compound = models.CharField('Состав коллекции', max_length=255, blank=True, null=True)
    pattern = models.CharField('Рисунок', max_length=255, blank=True, null=True)
    formats = models.CharField('Форматы', max_length=255, blank=True, null=True)
    style = models.CharField('Стиль', blank=True, null=True, max_length=255)
    description = models.TextField('Описание', blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, null=True, default='', verbose_name='Страна')
    popularity_score = models.PositiveBigIntegerField("Популярность от 1 до 10", default=1)
    number_of_elements = models.IntegerField('Количество элементов', default=3)
    image1 = models.ImageField('Изображение1', upload_to='collections/', blank=True, null=True)
    image2 = models.ImageField('Изображение2', upload_to='collections/', blank=True, null=True)
    image3 = models.ImageField('Изображение3', upload_to='collections/', blank=True, null=True)
    image4 = models.ImageField('Изображение4', upload_to='collections/', blank=True, null=True)
    image5 = models.ImageField('Изображение5', upload_to='collections/', blank=True, null=True)
    logo = models.ImageField('Логотип', upload_to='collections/logo/', blank=True, null=True)

    class Meta:
        verbose_name = 'Коллекция'
        verbose_name_plural = 'Коллекция'
    def __str__(self): return self.name

class Color(models.Model):
    name = models.CharField("Цвет", max_length=100)

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвет'

    def __str__(self): return self.name



class Material(models.Model):
    name = models.CharField("Материал", max_length=100)

    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материал'

    def __str__(self): return self.name

class Pattern(models.Model):
    name = models.CharField("Рисунок", max_length=100)

    class Meta:
        verbose_name = 'Рисунок'
        verbose_name_plural = 'Рисунок'

    def __str__(self): return self.name

class Room(models.Model):
    name = models.CharField("Помещение", max_length=100)

    class Meta:
        verbose_name = 'Помещение'
        verbose_name_plural = 'Помещение'

    def __str__(self): return self.name

class Form(models.Model):
    name = models.CharField("Форма", max_length=100)

    class Meta:
        verbose_name = 'Форма'
        verbose_name_plural = 'Форма'

    def __str__(self): return self.name

class Size(models.Model):
    name = models.CharField("Размер", max_length=100)

    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размер'

    def __str__(self): return self.name

class Style(models.Model):
    name = models.CharField("Стиль", max_length=100)

    class Meta:
        verbose_name = 'Стиль'
        verbose_name_plural = 'Стиль'

    def __str__(self): return self.name

class Surface(models.Model):
    name = models.CharField("Поверхность", max_length=100)

    class Meta:
        verbose_name = 'Поверхность'
        verbose_name_plural = 'Поверхность'

    def __str__(self): return self.name

class Purpose(models.Model):
    name = models.CharField("Назначение", max_length=100)

    class Meta:
        verbose_name = 'Назначение'
        verbose_name_plural = 'Назначение'

    def __str__(self): return self.name

class Feature(models.Model):
    name = models.CharField("Особенность", max_length=100)

    class Meta:
        verbose_name = 'Особенность'
        verbose_name_plural = 'Особенность'

    def __str__(self): return self.name


class Tile(models.Model):
    TILE_TYPES = [
        ('base', 'Базовая плитка'),
        ('border', 'Бордюр'),
        ('inlay', 'Вставка'),
        ('panel', 'Панно'),
        ('corner', 'Угловой элемент'),
        ('step', 'Ступень'),
        ('riser', 'Подступень'),
        ('plinth', 'Плинтус'),
        ('floor', 'напольная'),
    ]
    name = models.CharField("Название", max_length=255)
    description = models.TextField("Описание", blank=True, null=True)
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    discount = models.PositiveIntegerField("Скидка", default=0)
    image1 = models.ImageField(upload_to='tiles/', blank=True, null=True, verbose_name="Изображение 1")
    image2 = models.ImageField(upload_to='tiles/', blank=True, null=True, verbose_name="Изображение 2")
    image3 = models.ImageField(upload_to='tiles/', blank=True, null=True, verbose_name="Изображение 3")
    image4 = models.ImageField(upload_to='tiles/', blank=True, null=True, verbose_name="Изображение 4")
    image5 = models.ImageField(upload_to='tiles/', blank=True, null=True, verbose_name="Изображение 5")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    material = models.ForeignKey(Material, on_delete=models.SET_NULL, null=True, verbose_name="Материал")
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, verbose_name="Помещение")
    purpose = models.ManyToManyField(Purpose, verbose_name="Предназначение")
    size = models.ForeignKey(Size, on_delete=models.SET_NULL, null=True, verbose_name="Размер")
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True, verbose_name="Цвет")
    pattern = models.ForeignKey(Pattern, on_delete=models.SET_NULL, null=True, verbose_name="Рисунок")
    surface = models.ForeignKey(Surface, on_delete=models.SET_NULL, null=True, verbose_name="Поверхность на ощупь")
    form = models.ForeignKey(Form, on_delete=models.SET_NULL, null=True, verbose_name="Форма")
    is_new = models.BooleanField("Новинка", default=False)
    is_promo = models.BooleanField("Акция", default=False)
    is_large_format = models.BooleanField("Крупный формат", default=False)
    style = models.ForeignKey(Style, on_delete=models.SET_NULL, null=True, verbose_name="Стиль")
    features = models.ManyToManyField(Feature, verbose_name="Особенности")
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, verbose_name="Страна производитель")
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name='tiles', null=True, verbose_name="Коллекция")
    tile_type = models.CharField(max_length=10, choices=TILE_TYPES, default='base')
    popularity_score = models.IntegerField("Популярность от 1 до 10", default=1)
    

    class Meta:
        verbose_name = 'Плитка'
        verbose_name_plural = 'Плитка'

    def __str__(self): return self.name

class Slider(models.Model):
    title = models.CharField("Заголовок", max_length=255)
    description = models.TextField("Описание", blank=True)
    image = models.ImageField("Изображение", upload_to='slider_images/')
    is_published = models.BooleanField("Опубликовано", default=False)

    class Meta:
        verbose_name = 'Слайдер'
        verbose_name_plural = 'Слайдер'

    def __str__(self):
        return self.title
    
class Grout(models.Model):

    TYPE_CHOICES = [
        ("cement", "цементный"),
        ("epoxy", "эпоксидный"),
        ("polymeric", "полимерный"),
        ("polyurethane", "полиуритановый"),
        ("silicone", "силиконовый"),
    ]

    name = models.CharField("Название", max_length=255)
    color = models.CharField("Цвет", max_length=100)
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    type = models.CharField("Тип замазки", max_length=20, choices=TYPE_CHOICES, blank=True, null=True, default="")
    image1 = models.ImageField("Фотография 1", blank=True, null=True, upload_to='grouts/')
    image2 = models.ImageField("Фотография 2", blank=True, null=True, upload_to='grouts/')
    image3 = models.ImageField("Фотография 3", blank=True, null=True, upload_to='grouts/')
    image4 = models.ImageField("Фотография 4", blank=True, null=True, upload_to='grouts/')
    image5 = models.ImageField("Фотография 5", blank=True, null=True, upload_to='grouts/')

    class Meta:
        verbose_name = 'Замазка'
        verbose_name_plural = 'Замазка'

    def __str__(self):
        return f"{self.name} ({self.color})"