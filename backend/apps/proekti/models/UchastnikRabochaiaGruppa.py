from django.contrib.auth.models import User
from django.db import models

from apps.proekti.models import Proekt


class UchastnikRabochaiaGruppa(models.Model):
    class Meta():
        verbose_name = 'Участник рабочей группа'
        verbose_name_plural = 'Участники рабочей группы'

    proekt = models.ForeignKey(Proekt, verbose_name='Проект', on_delete=models.CASCADE)
    fio_uchastnika_gruppi = models.CharField('ФИО участника', max_length=255, null=True)
    dolznost_uchastnika_gruppi = models.CharField('Должность участника', max_length=255, null=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', null=True, blank=True, on_delete=models.SET_NULL)
    is_otvestveni = models.BooleanField('Отвественный', default=False)

    def __str__(self):
        return self.fio_uchastnika_gruppi
