from django.contrib import admin
from .models import Banner


class BannerAdmin(admin.ModelAdmin):
    fields = ['banner_pic']


admin.site.register(Banner, BannerAdmin)
