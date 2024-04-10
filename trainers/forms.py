from django import forms
from .models import Schedule


class ScheduleAdminForm(forms.ModelForm):
    day = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(), choices=Schedule.DAYS)
    