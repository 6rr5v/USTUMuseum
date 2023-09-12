from django.db import models


class Banner(models.Model):
    id = int
    banner_pic = models.ImageField(null=True, blank=True, upload_to="images/",
                                 verbose_name='Баннер')

    class Meta:
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннеры'