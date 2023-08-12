from django.shortcuts import render
from .models import Gallery, News
from django.views.generic import DetailView


def index(request):
    news_announcement = News.objects.order_by('-date')[:10]
    return render(request, 'main/index.html', {'news': news_announcement})


def news(request):
    news = News.objects.all()
    return render(request, 'news/news_home.html', {'news': news})


def authentication(request):
    return render(request, 'main/authentication.html')


def gallery(request):
    gal = Gallery.objects.all()
    return render(request, 'main/gallery.html', {'gallery': gal})


class NewsDetailView(DetailView):
    model = News
    template_name = 'news/detail_view.html'
    context_object_name = 'article'


def itm(request):
    return render(request, 'main/itm.html')


def excursion(request):
    return render(request, 'main/excursion.html')


def about(request):
    return render(request, 'main/about.html')
