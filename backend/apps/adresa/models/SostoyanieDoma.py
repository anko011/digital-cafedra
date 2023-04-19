from django.db import models

class SostoyanieDoma(models.Model):
    class Meta():
        verbose_name = 'Состояние дома'
        verbose_name_plural = 'Состояния дома'

    name = models.CharField('Состояние дома', max_length=255)

    def __str__(self):
        return f"{self.name or '-'}"
