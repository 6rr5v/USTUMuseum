from django.db import models


class Event(models.Model):
    id = int
    title_event = models.CharField('Название', max_length=100)
    announcement_event = models.CharField('Текст для карточки', max_length=150)
    picture_event = models.ImageField(null=True, blank=True, upload_to="images/",
                                 verbose_name='Изображение')
    date_event = models.DateField('Дата и время')

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'

    def __str__(self):
        return self.title_event

