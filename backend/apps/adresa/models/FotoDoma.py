from django.db import models

from apps.adresa.models import Dom


class FotoDoma(models.Model):
    class Meta():
        verbose_name = 'Фото дома'
        verbose_name_plural = 'Фото дома'

    foto = models.ImageField('Фото', )
    data = models.DateField('Дата фото', null=True, blank=True)
    dom = models.ForeignKey(Dom, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return 'фото'
