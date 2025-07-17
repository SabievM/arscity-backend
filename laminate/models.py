from django.db import models
from tile.models import Country, Category

class Grade(models.Model):
    name = models.CharField("Класс", max_length=100); 

    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Класс ламината'

    def __str__(self):
        return self.name

class Thickness(models.Model):
    name = models.CharField("Толщина", max_length=100); 

    class Meta:
        verbose_name = 'Толщина'
        verbose_name_plural = 'Толщина ламината'

    def __str__(self):
        return self.name

class Chamfer(models.Model):
    name = models.CharField("Фаска", max_length=100); 

    class Meta:
        verbose_name = 'Фаска'
        verbose_name_plural = 'Фаска ламината'

    def __str__(self):
        return self.name

class WaterResistance(models.Model):
    name = models.CharField("Влагостойкость", max_length=100); 

    class Meta:
        verbose_name = 'Влагостойкость'
        verbose_name_plural = 'Влагостойкость ламината'

    def __str__(self):
        return self.name

class LaminatePattern(models.Model):
    name = models.CharField("Тип рисунка", max_length=100); 

    class Meta:
        verbose_name = 'Тип рисунка'
        verbose_name_plural = 'Тип рисунка ламината'

    def __str__(self):
        return self.name

class Tone(models.Model):
    name = models.CharField("Оттенок", max_length=100); 

    class Meta:
        verbose_name = 'Оттенок'
        verbose_name_plural = 'Оттенок ламината'

    def __str__(self):
        return self.name

class WoodType(models.Model):
    name = models.CharField("Порода дерева", max_length=100); 

    class Meta:
        verbose_name = 'Порода дерева'
        verbose_name_plural = 'Порода дерева ламината'

    def __str__(self):
        return self.name

class Gloss(models.Model):
    name = models.CharField("Блеск", max_length=100); 

    class Meta:
        verbose_name = 'Блеск'
        verbose_name_plural = 'Блеск ламината'

    def __str__(self):
        return self.name

class Width(models.Model):
    name = models.CharField("Ширина", max_length=100); 

    class Meta:
        verbose_name = 'Ширина'
        verbose_name_plural = 'Ширина ламината'

    def __str__(self):
        return self.name

class Texture(models.Model):
    name = models.CharField("Поверхность на ощупь", max_length=100); 

    class Meta:
        verbose_name = 'Поверхность на ощупь'
        verbose_name_plural = 'Поверхность на ощупь ламината'

    def __str__(self):
        return self.name

class Construction(models.Model):
    name = models.CharField("Конструкция", max_length=100); 

    class Meta:
        verbose_name = 'Конструкция'
        verbose_name_plural = 'Конструкция ламината'

    def __str__(self):
        return self.name

class ConnectionType(models.Model):
    name = models.CharField("Тип соединения", max_length=100); 

    class Meta:
        verbose_name = 'Тип соединения'
        verbose_name_plural = 'Тип соединения ламината'

    def __str__(self):
        return self.name


class Laminate(models.Model):
    name = models.CharField("Название", max_length=255)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    discount = models.PositiveIntegerField("Скидка", default=0)
    quadrature = models.CharField("Количество квадратов в упаковке", max_length=255, blank=True, null=True)
    package_volume = models.CharField("Объем упаковки", max_length=255, blank=True, null=True)
    boards_in_packaging = models.IntegerField("Количество досок в упаковке", blank=True, null=True)
    board_dimensions = models.CharField("Размеры доски в мм", blank=True, null=True, max_length=255)
    package_weight = models.IntegerField("Вес упаковки", blank=True, null=True)
    color = models.CharField("Цвет", blank=True, null=True, max_length=255)
    image1 = models.ImageField(upload_to='laminates/', blank=True, null=True, verbose_name="Изображение 1")
    image2 = models.ImageField(upload_to='laminates/', blank=True, null=True, verbose_name="Изображение 2")
    image3 = models.ImageField(upload_to='laminates/', blank=True, null=True, verbose_name="Изображение 3")
    image4 = models.ImageField(upload_to='laminates/', blank=True, null=True, verbose_name="Изображение 4")
    image5 = models.ImageField(upload_to='laminates/', blank=True, null=True, verbose_name="Изображение 5")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, verbose_name="Страна производитель")
    grade = models.ForeignKey(Grade, on_delete=models.SET_NULL, null=True, verbose_name="Класс")
    thickness = models.ForeignKey(Thickness, on_delete=models.SET_NULL, null=True, verbose_name="Толщина")
    chamfer = models.ForeignKey(Chamfer, on_delete=models.SET_NULL, null=True, verbose_name="Фаска")
    water_resistance = models.ForeignKey(WaterResistance, on_delete=models.SET_NULL, null=True, verbose_name="Влагостойкость")
    laminate_pattern = models.ForeignKey(LaminatePattern, on_delete=models.SET_NULL, null=True, verbose_name="Рисунок")
    tone = models.ForeignKey(Tone, on_delete=models.SET_NULL, null=True, verbose_name="Оттенок")
    wood_type = models.ForeignKey(WoodType, on_delete=models.SET_NULL, null=True, verbose_name="Порода дерева")
    gloss = models.ForeignKey(Gloss, on_delete=models.SET_NULL, null=True, verbose_name="Блеск")
    width = models.ForeignKey(Width, on_delete=models.SET_NULL, null=True, verbose_name="Ширина")
    texture = models.ForeignKey(Texture, on_delete=models.SET_NULL, null=True, verbose_name="Поверхность на ощупь")
    is_substrate = models.BooleanField("Наличие подолжки", default=False)
    construction = models.ForeignKey(Construction, on_delete=models.SET_NULL, null=True, verbose_name="Конструкция")
    connection_type = models.ForeignKey(ConnectionType, on_delete=models.SET_NULL, null=True, verbose_name="Тип соединения")
    is_promo = models.BooleanField("Акция", default=False)
    type = models.CharField(default="laminate", max_length=255)

    class Meta:
        verbose_name = 'Ламинат'
        verbose_name_plural = 'Ламинат'

    def __str__(self): return self.name


class Underlay(models.Model):
    THICKNESS_CHOICES = [
        (2, "2 мм"),
        (3, "3 мм"),
        (5, "5 мм"),
    ]

    FLOOR_TYPE_CHOICES = [
        ('water', "Водяной пол"),
        ('electric', "Электрический пол"),
    ]
    name = models.CharField("Название", max_length=255)
    thickness = models.PositiveIntegerField("Толщина (мм)", choices=THICKNESS_CHOICES)
    has_vapor_barrier = models.BooleanField("С пароизоляцией", default=False)
    floor_type = models.CharField("Тип пола", max_length=20, choices=FLOOR_TYPE_CHOICES)
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    image1 = models.ImageField(upload_to='underlay/', blank=True, null=True, verbose_name="Изображение 1")
    image2 = models.ImageField(upload_to='underlay/', blank=True, null=True, verbose_name="Изображение 2")
    image3 = models.ImageField(upload_to='underlay/', blank=True, null=True, verbose_name="Изображение 3")
    image4 = models.ImageField(upload_to='underlay/', blank=True, null=True, verbose_name="Изображение 4")
    image5 = models.ImageField(upload_to='underlay/', blank=True, null=True, verbose_name="Изображение 5")
    type = models.CharField(default="underlay", max_length=255)
    

    class Meta:
        verbose_name = 'Подложка'
        verbose_name_plural = 'Подложка'

    def __str__(self):
        return f"{self.thickness} мм, {'с пароизоляцией' if self.has_vapor_barrier else 'без пароизоляции'}, {self.get_floor_type_display()}"
    

class SkirtingBoard(models.Model):
    TYPE_CHOICES = [
        ('mdf', 'МДФ'),
        ('aluminum', 'Алюминиевый'),
        ('duropolymer', 'Дюрополимер'),
        ('laminated', 'Ламинированный'),
        ('veneered', 'Шпонированный'),
    ]

    MOISTURE_RESISTANCE_CHOICES = [
        ('moisture', 'Влагостойкий'),
        ('waterproof', 'Водостойкий'),
    ]

    TONE_CHOICES = [
        ('light', 'Светлый'),
        ('dark', 'Темный'),
    ]

    name = models.CharField("Название", max_length=255)
    typematerial = models.CharField("Тип", max_length=20, choices=TYPE_CHOICES)
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    thickness = models.DecimalField("Толщина (мм)", max_digits=5, decimal_places=2)
    height = models.DecimalField("Высота (мм)", max_digits=5, decimal_places=2)
    moisture_resistance = models.CharField("Влагостойкость", max_length=20, choices=MOISTURE_RESISTANCE_CHOICES)
    tone = models.CharField("Оттенок", max_length=10, choices=TONE_CHOICES)
    image1 = models.ImageField(upload_to='skirtingBoard/', blank=True, null=True, verbose_name="Изображение 1")
    image2 = models.ImageField(upload_to='skirtingBoard/', blank=True, null=True, verbose_name="Изображение 2")
    image3= models.ImageField(upload_to='skirtingBoard/', blank=True, null=True, verbose_name="Изображение 3")
    image4 = models.ImageField(upload_to='skirtingBoard/', blank=True, null=True, verbose_name="Изображение 4")
    image5 = models.ImageField(upload_to='skirtingBoard/', blank=True, null=True, verbose_name="Изображение 5")
    type = models.CharField(default="skirtingboard", max_length=255)

    class Meta:
        verbose_name = 'Плинтус'
        verbose_name_plural = 'Плинтус'

    def __str__(self):
        return self.name