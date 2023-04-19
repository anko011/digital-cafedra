from django.db import models

from apps.proekti.models import UchastnikRabochaiaGruppa, StatusSoglasovania, \
    SoglosovaniePoProektu


class SoglosovaniePoProektuDetail(models.Model):
    class Meta():
        verbose_name = 'Согласование по проекту детализация'
        verbose_name_plural = 'Согласование по проекту детализация'

    soglosovanie_po_proektu = models.ForeignKey(SoglosovaniePoProektu, verbose_name='Согласование', on_delete=models.CASCADE)

    soglosushi = models.ForeignKey(UchastnikRabochaiaGruppa, verbose_name="Согласующий", null=True, blank=True, on_delete=models.SET_NULL)
    status_soglasovania = models.ForeignKey(StatusSoglasovania, verbose_name="Статус согласования", null=True, blank=True, on_delete=models.SET_NULL)

