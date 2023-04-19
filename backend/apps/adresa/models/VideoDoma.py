from django.db import models
from apps.adresa.models import Dom

class VideoDoma(models.Model):
    class Meta():
        verbose_name = 'Видео дома'
        verbose_name_plural = 'Видео дома'

    video = models.FileField('Видео', )
    data = models.DateField('Дата видео', null=True, blank=True)
    dom = models.ForeignKey(Dom, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return 'видео'
