from django.contrib import admin
from .models import Gallery, News


class GalleryAdmin(admin.ModelAdmin):
    fields = ['pic_url', 'descript']


admin.site.register(Gallery, GalleryAdmin)


class NewsAdmin(admin.ModelAdmin):
    fields = ['title', 'announcement', 'description', 'pictures', 'date']
    list_filter = ['date']


admin.site.register(News, NewsAdmin)
