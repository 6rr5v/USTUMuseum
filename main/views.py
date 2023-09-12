from django.shortcuts import render
from .models import Gallery, News
from events.models import Event
from banners.models import Banner
from django.views.generic import DetailView


def index(request):
    news_announcement = News.objects.order_by('-date')[:5]
    events_announcement = Event.objects.order_by('date_event')[:5]
    return render(request, 'main/index.html', {'news': news_announcement, 'events': events_announcement})


def news(request):
    news = News.objects.all()
    return render(request, 'news/news_home.html', {'news': news})


def events(request):
    event = Event.objects.order_by('date_event')
    return render(request, 'events/events.html', {'events': event})


def authentication(request):
    return render(request, 'main/authentication.html')


def gallery(request):
    gal = Gallery.objects.all()
    return render(request, 'main/gallery.html', {'gallery': gal})


class NewsDetailView(DetailView):
    model = News
    template_name = 'news/detail_view.html'
    context_object_name = 'article'


def excursion(request):
    return render(request, 'main/excursion.html')


def about(request):
    return render(request, 'main/about.html')
