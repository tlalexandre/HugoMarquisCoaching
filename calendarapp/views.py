from django.views.generic import TemplateView
from django.http import JsonResponse
from django.shortcuts import render
from .models import Course,PrivateSession


# Create your views here.

class BookingsView(TemplateView):
    template_name = 'bookings.html'


def get_events(request):
    events = Course.objects.all()
    event_list = []
    for event in events:
        event_list.append({
            'title':event.name,
            'start': event.start_time.strftime('%Y-%m-%dT%H:%M:%S'),
            'end': event.end_time.strftime('%Y-%m-%dT%H:%M:%S'),
            'day':event.day_of_the_week,
            'description': event.description,
            'participants': event.actual_participants,
            'maxParticipants': event.max_participants,
            'location':event.location,
        })
    return JsonResponse(event_list, safe=False)