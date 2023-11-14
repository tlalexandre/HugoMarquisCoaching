from django.views.generic import TemplateView


# Create your views here.

class BookingsView(TemplateView):
    template_name = 'bookings.html'
