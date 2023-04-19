from django.db import models

from apps.adresa.models import Uliza, SostoyanieDoma, TipObecta
from apps.vladelzi_zdani.models import VladelezZdania, Zastroyshik


class Dom(models.Model):
    class Meta():
        verbose_name = 'Дом'
        verbose_name_plural = 'Дома'

    uliza = models.ForeignKey(Uliza, verbose_name='Улица', on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField('Номер дома', max_length=255)
    etazhnost = models.IntegerField('Этажность', null=True, blank=True)
    ploshad = models.FloatField('Площадь', null=True, blank=True)
    god_realizazii = models.IntegerField('Год реализации', null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
    json_dadata = models.TextField(null=True, blank=True)
    vladelez_zdania = models.ForeignKey(VladelezZdania, verbose_name='Владелец здания', on_delete=models.SET_NULL,
                                        null=True, blank=True)
    zastroyshik = models.ForeignKey(Zastroyshik, verbose_name='Застройщик', on_delete=models.SET_NULL, null=True,
                                    blank=True)
    tip_obecta = models.ForeignKey(TipObecta, verbose_name='Тип объекта', on_delete=models.SET_NULL, null=True,
                                   blank=True)
    sostoyanie_doma = models.ForeignKey(SostoyanieDoma, verbose_name='Состояние дома', on_delete=models.SET_NULL,
                                        null=True, blank=True)
    flat_cadnum = models.CharField('Кдастровый номер', max_length=20, null=True, blank=True)

    def __str__(self):
        return self.get_full_adres()

    def get_full_adres(self):
        okrug = ''
        naseleni_punkt = ''
        rayon = ''
        uliza = ''
        if self.uliza:
            uliza = self.uliza.name
            if self.uliza.rayon:
                rayon = self.uliza.rayon.name + ' район,'
                if self.uliza.rayon.naseleni_punkt:
                    naseleni_punkt = self.uliza.rayon.naseleni_punkt.name + ','
                    if self.uliza.rayon.naseleni_punkt.okrug:
                        okrug = self.uliza.rayon.naseleni_punkt.okrug.name + ','
        return f'{okrug} {naseleni_punkt} {rayon} {uliza} {self.name or ""}'

    def get_rayon(self):
        if self.uliza:
            if self.uliza.rayon:
                return self.uliza.rayon
        return None