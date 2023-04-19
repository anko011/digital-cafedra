from django.db import models

class TipObecta(models.Model):
    class Meta():
        verbose_name = 'Тип объекта'
        verbose_name_plural = 'Типы объектов'

    name = models.CharField('Тип объекта', max_length=255)

    def __str__(self):
        return f"{self.name or '-'}"
