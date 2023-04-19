from django.db import models

from apps.adresa.models import NaseleniPunkt


class Rayon(models.Model):
    class Meta():
        verbose_name = 'Район'
        verbose_name_plural = 'Районы'

    name = models.CharField('Название района', max_length=255)
    naseleni_punkt = models.ForeignKey(NaseleniPunkt, verbose_name='Населенный пункт', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.name or '-'}"
