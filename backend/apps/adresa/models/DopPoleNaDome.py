
from django.db import models

from apps.adresa.models import Dom, DopPoleDoma


class DopPoleNaDome(models.Model):
    class Meta():
        verbose_name = 'Доп поле для домов'
        verbose_name_plural = 'Доп поля для домов'

    dop_pole_doma = models.ForeignKey(DopPoleDoma, verbose_name='Доп поле дома', on_delete=models.CASCADE)
    dom = models.ForeignKey(Dom, verbose_name='Дом', on_delete=models.CASCADE)
    znachenie = models.CharField('Значение', null=True, blank=True, max_length=255)

    def __str__(self):
        return f'{self.dom.get_full_adres()} {self.dop_pole_doma.name}'
