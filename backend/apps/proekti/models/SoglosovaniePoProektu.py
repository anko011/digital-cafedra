from django.db import models

from apps.adresa.models import Dom
from apps.proekti.models import Proekt, TipResheniaPoProektu, UchastnikRabochaiaGruppa, StatusSoglasovania


class SoglosovaniePoProektu(models.Model):
    class Meta():
        verbose_name = 'Согласование по проекту'
        verbose_name_plural = 'Решение по проекту'

    proekt = models.ForeignKey(Proekt, verbose_name='Проект', on_delete=models.CASCADE)
    dom = models.ForeignKey(Dom, verbose_name='Дом', on_delete=models.PROTECT)
    tip_reshenia_po_proektu = models.ForeignKey(TipResheniaPoProektu, on_delete=models.SET_NULL, null=True, blank=True)
    data_priniatia_reshenia = models.DateField('Дата принятия решения', null=True, blank=True)

    scan_documenta = models.FileField('Скан документа', null=True, blank=True)

    def __str__(self):
        return f'Согласование по проекту {self.dom.get_full_adres()}'
