from django.db import models


class News(models.Model):
    id_news = int
    title = models.CharField('Название', max_length=100)
    announcement = models.CharField('Текст для карточки', max_length=150)
    description = models.TextField('Описание')
    pictures = models.ImageField(null=True, blank=True, upload_to="images/",
                                 verbose_name='Изображение')
    date = models.DateField('Дата и время')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title


class Gallery(models.Model):
    id = int
    pic_url = models.ImageField(null=True, blank=True, upload_to="images/", verbose_name='Фотография')
    descript = models.CharField('Краткое описание', max_length=50, null=True)

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галерея'

    def __str__(self):
        return self.descript
