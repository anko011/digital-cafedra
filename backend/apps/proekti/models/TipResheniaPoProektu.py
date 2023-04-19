from django.db import models

class TipResheniaPoProektu(models.Model):
    class Meta():
        verbose_name = 'Тип решения по проекту'
        verbose_name_plural = 'Тип решения по проекту'

    nazvanie = models.CharField('Название', max_length=255, )

    def __str__(self):
        return self.nazvanie