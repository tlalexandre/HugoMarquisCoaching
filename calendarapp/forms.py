from django import forms
from crispy_forms.helper import FormHelper
from .models import Course, PrivateSession, UnavailablePeriod, DAYS_OF_WEEK


description_attrs = {
    'rows': 4,
    'cols': 25,
    'class': 'noresize',
    'placeholder': 'Enter a description for the course here...'
}


class DateTimeInput(forms.DateTimeInput):
    """ Widget for datetime input """
    input_type = 'datetime-local'
    format = '%Y-%m-%dT%H:%M'


class UnavailablePeriodForm(forms.ModelForm):
    """ Form for unavailable periods """
    start_time = forms.DateTimeField(
        input_formats=['%Y-%m-%dT%H:%M'], widget=DateTimeInput())
    end_time = forms.DateTimeField(
        input_formats=['%Y-%m-%dT%H:%M'], widget=DateTimeInput())

    class Meta:
        model = UnavailablePeriod
        fields = ['start_time', 'end_time']

    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')

        if end_time and start_time and end_time < start_time:
            raise forms.ValidationError(
                "End time cannot be earlier than start time.")

        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)


class CourseForm(forms.ModelForm):
    """ Form for courses """
    start_time = forms.DateTimeField(
        input_formats=['%Y-%m-%dT%H:%M'], widget=DateTimeInput())
    end_time = forms.DateTimeField(
        input_formats=['%Y-%m-%dT%H:%M'], widget=DateTimeInput())
    description = forms.CharField(
        widget=forms.Textarea(attrs=description_attrs))
    location = forms.CharField()
    max_participants = forms.IntegerField(
        min_value=1, max_value=100, widget=forms.NumberInput())
    is_recurrent = forms.BooleanField(required=False)

    class Meta:
        model = Course
        fields = ['name', 'description', 'start_time', 'end_time',
                  'location', 'max_participants', 'is_recurrent']

    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')

        if end_time and start_time and end_time < start_time:
            raise forms.ValidationError(
                "End time cannot be earlier than start time.")

        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)


class PrivateSessionForm(forms.ModelForm):
    """ Form for private sessions """
    start_time = forms.DateTimeField(
        input_formats=['%Y-%m-%dT%H:%M'], widget=DateTimeInput())
    end_time = forms.DateTimeField(
        input_formats=['%Y-%m-%dT%H:%M'], widget=DateTimeInput())

    class Meta:
        model = PrivateSession
        fields = ['name', 'start_time', 'end_time',
                  'location', 'description', 'type']

    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')

        if end_time and start_time and end_time < start_time:
            raise forms.ValidationError(
                "End time cannot be earlier than start time.")

        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
