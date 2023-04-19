from django.db import models

from apps.proekti.models import StatusIspolnenia


class Proekt(models.Model):
    class Meta():
        verbose_name = 'Проект'
        verbose_name_plural = 'Проект'

    vnutrinii_nomer = models.CharField('Внутренний номер', max_length=255, null=True, blank=True )
    data_nachala_proekta = models.DateField('Дата начала проекта', null=True, blank=True )
    primechanie = models.TextField('Примечание', null=True, blank=True )
    status_ispolnenia = models.ForeignKey(StatusIspolnenia, verbose_name='Статус исполения решения', null=True,
                                          blank=True, on_delete=models.SET_NULL)


    def __str__(self):
        result = self.vnutrinii_nomer if self.vnutrinii_nomer else self.id
        return f'Проект #{result}'

    def get_adresa(self):
        reesult = []
        for i in self.resheniepoproektu_set.all():
            reesult.append(i.dom.get_full_adres())
        return reesult