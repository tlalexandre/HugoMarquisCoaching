from .  import views
from django.urls import path
from .views import get_events

urlpatterns=[
    path('',views.BookingsView.as_view(),name='bookings'),
    path('get_events/', get_events, name='get_events'),
]