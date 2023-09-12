from django.shortcuts import render
from .models import Event


def events(request):
    event_announcement = Event.objects.order_by('date_event')[:5]
    return render(request, 'main/index.html', {'events': event_announcement})

