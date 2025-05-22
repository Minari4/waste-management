from django import forms
from .models import IllegalDumpingReport

class IllegalDumpingReportForm(forms.ModelForm):
    class Meta:
        model = IllegalDumpingReport
        fields = ['location', 'latitude', 'longitude', 'description', 'photo']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        }