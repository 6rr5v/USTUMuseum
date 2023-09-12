from django.shortcuts import render
from .models import Banner


def vision (request):
    banners = Banner.objects.order_by('id').all()
    return render('visions.html', {'banners': banners})
