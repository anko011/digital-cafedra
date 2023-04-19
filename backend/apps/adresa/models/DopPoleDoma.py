
from django.db import models

from apps.adresa.models import Dom


class DopPoleDoma(models.Model):
    class Meta():
        verbose_name = 'Доп поле для домов'
        verbose_name_plural = 'Доп поля для домов'

    name = models.CharField('Название', max_length=255)

    def __str__(self):
        return self.name
