from django.db import models

class Okrug(models.Model):
    class Meta():
        verbose_name = 'Округ'
        verbose_name_plural = 'Округа'

    name = models.CharField('Название округа', max_length=255)

    def __str__(self):
        return f"{self.name or '-'}"
