from django.db import models
from apps.adresa.models import Rayon


class Uliza(models.Model):
    class Meta():
        verbose_name = 'Улица'
        verbose_name_plural = 'Улицы'

    name = models.CharField('Название', max_length=255)
    rayon = models.ForeignKey(Rayon, verbose_name='Район', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.name or '-'}"
