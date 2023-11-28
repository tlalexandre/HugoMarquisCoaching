from django.views.generic import TemplateView
from django.views import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse,Http404
from django.utils.text import slugify
from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import ValidationError
from .models import Course,PrivateSession
from .forms import CourseForm, PrivateSessionForm

@login_required
def join_course(request, course_id):
    if request.method == 'POST':
        course = get_object_or_404(Course, id=course_id)
        try:
            course.add_participant(request.user)
            return JsonResponse({'message': 'You have successfully joined the course.'})
        except ValidationError:
            return JsonResponse({'message': 'This course is full.'}, status=400)

def update_course(request,course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        course.name = request.POST.get('name')
        course.description = request.POST.get('description')
        course.start_time = request.POST.get('start_time')
        course.end_time = request.POST.get('end_time')
        course.location = request.POST.get('location')
        course.max_participants = request.POST.get('max_participants')
        course.type = request.POST.get('type')
        course.save()
        return redirect("bookings")
    else:
        return render(request, 'event_update.html', {'event': course})

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
    try:
        # Try to get a PrivateSession with the given slug
        private_session = PrivateSession.objects.get(slug=slug)

        # Check if the user has permission to view the private session
        if not private_session.is_creator(request.user) and not request.user.is_superuser:
            context = {'private_session': None}
            return render(request, 'event_details.html', context)
        
        context = {'private_session': private_session}
        return render(request, 'event_details.html', context)

    except PrivateSession.DoesNotExist:
        pass  # PrivateSession not found, proceed to check for Course

    # Check if the slug is "undefined" and handle it
    if slug == "undefined":
        context = {'private_session': None}  # Set context to show the modal
        return render(request, 'event_details.html', context)

    try:
        # Try to get a Course with the given slug
        course = Course.objects.get(slug=slug)
        context = {'course': course}
        return render(request, 'event_details.html', context)
    
    except Course.DoesNotExist:
        # If neither Course nor PrivateSession is found, return a 404
        raise Http404("No Course or PrivateSession matches the given query.")
        

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
            'participants':list(event.participants.values_list('id', flat=True)),
            'maxParticipants': event.max_participants,
            'location':event.location,
            'slug':event.slug,
        })
    return JsonResponse(event_list, safe=False)


def get_private_sessions(request):
    events = PrivateSession.objects.all()
    event_list = []
    for event in events:
        if event.is_creator(request.user) or request.user.is_superuser:
            event_list.append({
                'title':event.name,
                'start': event.start_time.strftime('%Y-%m-%dT%H:%M:%S'),
                'end': event.end_time.strftime('%Y-%m-%dT%H:%M:%S'),
                'location':event.location,
                'slug':event.slug,
            })
        else:
            event_list.append({
                'title':"Private Session",
                'start': event.start_time.strftime('%Y-%m-%dT%H:%M:%S'),
                'end': event.end_time.strftime('%Y-%m-%dT%H:%M:%S'),
            })
    return JsonResponse(event_list, safe=False)

# def view_private_session(request, session_id):
#     session = PrivateSession.objects.get(id=session_id)
#     if not session.is_creator(request.user):
#         messages.error(request, 'You do not have permission to view this session.')
#         return redirect('bookings')