from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('gallery/', views.gallery, name='gallery'),
    path('itm/', views.itm, name='itm'),
    path('excursion/', views.excursion, name='excursion'),
    path('about/', views.about, name='about'),
    path('news/', views.news, name='news'),
    path('news/<int:pk>', views.NewsDetailView.as_view(), name='news-detail'),
]
