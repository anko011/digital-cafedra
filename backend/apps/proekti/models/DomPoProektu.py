from django.db import models

from apps.adresa.models import Dom
from apps.proekti.models import Proekt


class DomPoProektu(models.Model):
    class Meta():
        verbose_name = 'Дом по проекту'
        verbose_name_plural = 'Дома по проекту'

    proekt = models.ForeignKey(Proekt, verbose_name='Проект', on_delete=models.CASCADE)
    dom = models.ForeignKey(Dom, verbose_name='Дом', on_delete=models.PROTECT)

    def __str__(self):
        return f'Дом по проекту {self.dom.get_full_adres()}'
