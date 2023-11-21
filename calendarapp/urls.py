from .  import views
from django.urls import path
from .views import get_courses,get_private_sessions,event_detail

urlpatterns=[
    path('',views.BookingsView.as_view(),name='bookings'),
    path('get_courses/', get_courses, name='get_courses'),
    path('get_private_sessions/', get_private_sessions, name='get_private_sessions'),
    path('event_detail/<slug>/', event_detail, name='event_detail'),
]