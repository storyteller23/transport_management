from django import forms
from .models import Report

class ReportCreationForm(forms.ModelForm):

    class Meta:
        model = Report
        fields = ('date', 'transport', 'fuel_dispended', 'fuel_used', 'mileage')