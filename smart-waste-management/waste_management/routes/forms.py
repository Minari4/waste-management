from django import forms
from .models import CollectionRoute

class CollectionRouteForm(forms.ModelForm):
    class Meta:
        model = CollectionRoute
        fields = [
            'name', 'description', 'assigned_to', 'collection_day', 'is_active',
            'point_a_latitude', 'point_a_longitude', 'point_b_latitude', 'point_b_longitude'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'assigned_to': forms.Select(attrs={'class': 'form-select'}),
            'collection_day': forms.TextInput(attrs={  # Changed to TextInput
                'class': 'form-control',
                'placeholder': 'Enter collection day (e.g., Monday, Tuesday)'
            }),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'point_a_latitude': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Latitude of Point A',
                'step': '0.000001'
            }),
            'point_a_longitude': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Longitude of Point A',
                'step': '0.000001'
            }),
            'point_b_latitude': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Latitude of Point B',
                'step': '0.000001'
            }),
            'point_b_longitude': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Longitude of Point B',
                'step': '0.000001'
            }),
        }