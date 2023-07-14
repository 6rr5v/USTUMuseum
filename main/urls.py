from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('authentication/', views.authentication, name='auth'),
    path('gallery/', views.gallery, name='gallery'),
    path('itm/', views.itm, name='itm'),
    path('excursion/', views.excursion, name='excursion'),
    path ('about/', views.about, name='about')
]
