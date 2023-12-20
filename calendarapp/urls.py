from . import views
from django.urls import path
from .views import (
    get_all_events,
    get_courses,
    get_private_sessions,
    event_detail,
    event_create,
    join_course,
    update_course,
    delete_course,
    add_unavailable_period,
    approve_private_session,
    delete_private_session
)

urlpatterns = [
    path('', views.bookings_view, name='bookings'),
    path('get_courses/', get_courses, name='get_courses'),
    path('get_private_sessions/', get_private_sessions,
         name='get_private_sessions'),
    path('get_all_events/', get_all_events,
         name='get_all_events'),  # Add this line
    path('event_detail/<slug>/', event_detail, name='event_detail'),
    path('event_create/', event_create, name='event_create'),
    path('join_course/<slug:slug>/', views.join_course, name='join_course'),
    path('update_course/<int:course_id>/',
         update_course,
         name='update_course'),
    path('delete_course/<int:course_id>/',
         delete_course,
         name='delete_course'),
    path(
        'unavailable_period/add/',
        add_unavailable_period,
        name='add_unavailable_period'
    ),
    path(
        'private_session/<slug:slug>/approve',
        approve_private_session,
        name='approve_private_session'
    ),
    path(
        'bookings/private_session/<slug:slug>/delete',
        delete_private_session,
        name='delete_private_session'
    ),
]
