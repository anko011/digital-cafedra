from django.db import models


class TipVladelza(models.Model):
    class Meta():
        verbose_name = 'Тип владельца'
        verbose_name_plural = 'Тип владельца'

    nazvanie = models.CharField('Название', max_length=255)

    def __str__(self):
        return self.nazvanie
