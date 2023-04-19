
from django.db import models

class DopPoleProekta(models.Model):
    class Meta():
        verbose_name = 'Доп поле для проекта'
        verbose_name_plural = 'Доп поля для проекта'

    name = models.CharField('Название', max_length=255)

    def __str__(self):
        return self.name
