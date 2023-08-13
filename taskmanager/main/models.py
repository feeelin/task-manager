from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    text = models.TextField('Описание')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
