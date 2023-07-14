from django.db import models

class Articles(models.Model):
    title = models.CharField('Название', max_length=100)
    description = models.TextField('Описание')
    date = models.DateTimeField('Дата и время')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
