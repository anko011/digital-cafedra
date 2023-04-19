from django.db import models

from apps.adresa.models import Okrug


class NaseleniPunkt(models.Model):
    class Meta():
        verbose_name = 'Населенный пунт'
        verbose_name_plural = 'Населеные пункты'

    name = models.CharField('Название', max_length=255)
    okrug = models.ForeignKey(Okrug,  verbose_name='Округ', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        okrug = ''
        if self.okrug:
            okrug = self.okrug.name
        return f"{okrug} {self.name or '-'}"