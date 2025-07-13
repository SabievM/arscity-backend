from django.db import models


class Advice(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")

    class Meta:
        verbose_name = "Полезные советы"
        verbose_name_plural = "Полезные советы"

    def __str__(self):
        return self.title