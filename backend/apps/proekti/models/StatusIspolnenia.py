from django.db import models

class StatusIspolnenia(models.Model):
    class Meta():
        verbose_name = 'Статус исполнения'
        verbose_name_plural = 'Статус исполнения'

    nazvanie = models.CharField('Название', max_length=255, )

    def __str__(self):
        return self.nazvanie