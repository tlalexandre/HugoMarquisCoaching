from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.utils.text import slugify
from django.shortcuts import render, get_object_or_404, redirect
from .models import Course,PrivateSession
from .forms import CourseForm, PrivateSessionForm


# Create your views here.
@login_required
def event_create(request):
    if request.user.is_superuser:
        Form = CourseForm
    else:
        Form = PrivateSessionForm

    if request.method == 'POST':
        print("POST request received")
        form = Form(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.slug = slugify(instance.name)
            instance.save()
            return redirect('bookings')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    print(f"Error in field {field}: {error}")
    else:
        form = Form()
    return render(request, 'event_create.html', {'form': form})

def event_detail(request, slug):
    # Try to get a Course with the given slug
    try:
        course = Course.objects.get(slug=slug)
        context = {'course': course}
        return render(request, 'event_details.html', context)
    except Course.DoesNotExist:
        pass  # Course not found, proceed to try to get a PrivateSession

    # Try to get a PrivateSession with the given slug
    try:
        private_session = PrivateSession.objects.get(slug=slug)
        context = {'private_session': private_session}
        return render(request, 'event_details.html', context)
    except PrivateSession.DoesNotExist:
        # If neither Course nor PrivateSession is found, return a 404
        raise Http404("No Course or PrivateSession matches the given query.")
        
# class BookingsView(TemplateView):
#     template_name = 'bookings.html'

def bookings_view(request):
    return render(request, 'bookings.html')

def get_courses(request):
    events = Course.objects.all()
    event_list = []
    for event in events:
        event_list.append({
            'title':event.name,
            'start': event.start_time.strftime('%Y-%m-%dT%H:%M:%S'),
            'end': event.end_time.strftime('%Y-%m-%dT%H:%M:%S'),
            'description': event.description,
            'participants': event.actual_participants,
            'maxParticipants': event.max_participants,
            'location':event.location,
            'slug':event.slug,
        })
    return JsonResponse(event_list, safe=False)


def get_private_sessions(request):
    events = PrivateSession.objects.all()
    event_list = []
    for event in events:
        event_list.append({
            'title':event.name,
            'start': event.start_time.strftime('%Y-%m-%dT%H:%M:%S'),
            'end': event.end_time.strftime('%Y-%m-%dT%H:%M:%S'),
            'slug':event.slug,
        })
    return JsonResponse(event_list, safe=False)