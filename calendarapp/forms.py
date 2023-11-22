from django import forms
from crispy_forms.helper import FormHelper
from .models import Course, PrivateSession

class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'description', 'start_time', 'end_time', 'location', 'type', 'max_participants']
        widgets = {
            'start_time': DateTimeInput(),
            'end_time': DateTimeInput(),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)

class PrivateSessionForm(forms.ModelForm):
    class Meta:
        model = PrivateSession
        fields = ['name', 'start_time', 'end_time', 'location', 'type']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
