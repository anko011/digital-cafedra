from django.db import models


class Zastroyshik(models.Model):
    class Meta():
        verbose_name = 'Застройщик'
        verbose_name_plural = 'Застройщики'

    nazvanie = models.CharField('Название', max_length=255)

    def __str__(self):
        return self.nazvanie
