from django.db import models


class StatusSoglasovania(models.Model):
    class Meta():
        verbose_name = 'Статус согласования'
        verbose_name_plural = 'Статусы согласования'

    nazvanie = models.CharField('Название', max_length=255)


    def __str__(self):
        return self.nazvanie
