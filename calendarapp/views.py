from django.views.generic import TemplateView
from django.views.decorators.http import require_POST
from django.views import View
from django.contrib import messages
from django.utils.translation import gettext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse,Http404, HttpResponseBadRequest
from django.utils.text import slugify
from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from .models import Course,PrivateSession,UnavailablePeriod,User
from .forms import CourseForm, PrivateSessionForm, UnavailablePeriodForm
from .utils import check_overlap
from itertools import chain

def unavailable_period(request):
    superuser = User.objects.get(is_superuser=True)
    periods = UnavailablePeriod.objects.filter(user=superuser)
    return render(request, 'unavailable_periods.html', {'periods': periods})

def add_unavailable_period(request):
    superuser = User.objects.get(is_superuser=True)
    date = request.GET.get('date')
    if request.method == 'POST':
        form = UnavailablePeriodForm(request.POST)
        if form.is_valid():
            start_time = form.cleaned_data.get('start_time')
            end_time = form.cleaned_data.get('end_time')

            if check_overlap(start_time, end_time, Course) or \
               check_overlap(start_time, end_time, PrivateSession) or \
               check_overlap(start_time, end_time, UnavailablePeriod):
                form.add_error(None, gettext('An event already exists within this time period.'))
            else:
                period = form.save(commit=False)
                period.user = superuser
                period.save()
                messages.success(request, gettext('Your unavailable period was successfully added.'))
                return redirect('bookings')
    else:
        form = UnavailablePeriodForm(initial={'date': date})
    return render(request, 'add_unavailable_period.html', {'form': form})

@login_required
def join_course(request, slug):
    if request.method == 'POST':
        course = get_object_or_404(Course, slug=slug)
        if course.participants.filter(id=request.user.id).exists():
            messages.info(request, gettext('You have already joined this course.'))
            return redirect('event_detail', slug=course.slug)
        try:
            course.add_participant(request.user)
            messages.success(request, gettext('You have successfully joined the course.'))
            return redirect('event_detail', slug=course.slug)
        except ValidationError:
            messages.error(request, gettext('This course is full.'))
            return redirect('event_detail', slug=course.slug)

def update_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            start_time = form.cleaned_data.get('start_time')
            end_time = form.cleaned_data.get('end_time')

            if check_overlap(start_time, end_time, Course, course_id) or \
               check_overlap(start_time, end_time, PrivateSession) or \
               check_overlap(start_time, end_time, UnavailablePeriod):
                form.add_error(None, gettext('An event already exists within this time period.'))
            else:
                form.save()
                messages.success(request, gettext('The course has been successfully updated.'))
                # Get the users who joined the course
                users = course.participants.all()
                # Send an email to each user
                for user in users:
                    message=(
                        gettext('The course you joined has been updated.'
                        f' It is now starting at {course.start_time} and ending at {course.end_time}.'
                        f' The location is {course.location}.')
                    )
                    send_mail(
                       gettext( f'Course {course.name} Updated'),
                        message,
                        'from@example.com',
                        [user.email],
                        fail_silently=False,
                    )
                return redirect("bookings")
        else:
            return render(request, 'event_update.html', {'event': course, 'form': form})
    else:
        form = CourseForm(instance=course)
        return render(request, 'event_update.html', {'event': course, 'form': form})


@login_required
def delete_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.user.is_superuser:
        # Get the users who joined the course
        users = course.participants.all()
        course_name=course.name
        # Delete the course
        # Send an email to each user
        for user in users:
            try:
                send_mail(
                    gettext(f'Course {course_name} Deleted'),
                    gettext('The course you joined has been deleted.'),
                    'from@example.com',
                    [user.email],
                    fail_silently=False,
                )
                print(f"Email sent to {user.email}")
            except Exception as e:
                print(f"Failed to send email to {user.email}: {e}")
        course.delete()
        messages.success(request, gettext('The course has been successfully deleted.'))
        return redirect('bookings')
    else:
        return HttpResponseForbidden()

# Create your views here.
@login_required
def event_create(request):
    print(request.GET)
    event_type = request.GET.get('type')
    print(event_type)
    if event_type == 'course':
        Form = CourseForm
    elif event_type == 'private_session':
        Form = PrivateSessionForm
    else:
        return HttpResponseBadRequest('Invalid event type')

    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            start_time = form.cleaned_data.get('start_time')
            end_time = form.cleaned_data.get('end_time')

            if check_overlap(start_time, end_time, Course) or \
               check_overlap(start_time, end_time, PrivateSession) or \
               check_overlap(start_time, end_time, UnavailablePeriod):
                form.add_error(None, gettext('An event already exists within this time period.'))
            else:
                instance = form.save(commit=False)
                instance.user = request.user
                instance.slug = slugify(instance.name)
                instance.save()
                if isinstance(instance,PrivateSession):
                    messages.success(request, gettext('Your private session has been created and is pending approval.'))
                else:
                    messages.success(request, gettext('Your course has been created.'))
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
        pass  # Course not found, proceed to check for UnavailablePeriod

    try:
        # Try to get an UnavailablePeriod with the given slug
        unavailable_period = UnavailablePeriod.objects.get(slug=slug)
        context = {'unavailable_period': unavailable_period}
        return render(request, 'unavailable_periods.html', context)

    except UnavailablePeriod.DoesNotExist:
        # If neither Course, PrivateSession, nor UnavailablePeriod is found, return a 404
        raise Http404("No Course, PrivateSession, or UnavailablePeriod matches the given query.")
        

def bookings_view(request):
    context = {
        'is_superuser': request.user.is_superuser,
    }
    return render(request, 'bookings.html', context)

def get_courses(request):
    courses = Course.objects.all()
    course_list = []
    for course in courses:
        course_list.append({
            'title':course.name,
            'start': course.start_time.strftime('%Y-%m-%dT%H:%M:%S'),
            'end': course.end_time.strftime('%Y-%m-%dT%H:%M:%S'),
            'description': course.description,
            'participants':list(course.participants.values_list('id', flat=True)),
            'maxParticipants': course.max_participants,
            'location':course.location,
            'slug':course.slug,
            'color': '#ffc107',  # Or any color you want
            
        })
    return course_list


@require_POST
def approve_private_session(request,slug):
    private_session = PrivateSession.objects.get(slug=slug)
    if request.user.is_superuser:
        private_session.approve()
        try:
            send_mail(
                    gettext('Your private session has been approved'),
                    gettext('Your private session titled "{}" has been approved.').format(private_session.name),
                    'from@example.com',
                    [private_session.user.email],
                    fail_silently=False,
                )
            print(f"Email sent to {private_session.user.email}")
        except Exception as e:
            print(f"Failed to send email to {private_session.user.email}: {e}")
    return redirect('event_detail', slug=slug)


@require_POST
def delete_private_session(request, slug):
    private_session = get_object_or_404(PrivateSession, slug=slug)
    if request.user.is_superuser or request.user == private_session.user:
        try:
            send_mail(
                gettext('Your private session has been deleted'),
                gettext('Your private session titled "{}" has been deleted.').format(private_session.name),
                'from@example.com',
                [private_session.user.email],
                fail_silently=False,
            )
            print(f"Email sent to {private_session.user.email}")
        except Exception as e:
                print(f"Failed to send email to {private_session.user.email}: {e}")
        private_session.delete()
    return redirect('bookings')


def get_private_sessions(request):
    private_sessions = PrivateSession.objects.all()
    private_session_list = []
    for private_session in private_sessions:
        if private_session.is_creator(request.user) or request.user.is_superuser:
            private_session_list.append({
                'title': private_session.name,
                'start': private_session.start_time.strftime('%Y-%m-%dT%H:%M:%S'),
                'end': private_session.end_time.strftime('%Y-%m-%dT%H:%M:%S'),
                'location': private_session.location,
                'slug': private_session.slug,
                'color': '#28a745' if private_session.is_approved else '#007bff',
            })
        else:
            private_session_list.append({
                'title': "Private Session",
                'start': private_session.start_time.strftime('%Y-%m-%dT%H:%M:%S'),
                'end': private_session.end_time.strftime('%Y-%m-%dT%H:%M:%S'),
                'color':'#dc3545',
            })
    return private_session_list

def get_unavailable_periods(request):
    superuser = User.objects.get(is_superuser=True)
    periods = UnavailablePeriod.objects.filter(user=superuser)
    period_list = []
    for period in periods:
        period_list.append({
            'title': 'Unavailable',
            'start': period.start_time.strftime('%Y-%m-%dT%H:%M:%S'),
            'end': period.end_time.strftime('%Y-%m-%dT%H:%M:%S'),
            'slug': period.slug,
            'color': '#6c757d',  # Or any color you want
        })
    return period_list

def get_all_events(request):
    courses = get_courses(request)
    private_sessions = get_private_sessions(request)
    unavailable_periods = get_unavailable_periods(request)
    all_events = list(chain(courses, private_sessions, unavailable_periods))
    return JsonResponse(all_events, safe=False)

