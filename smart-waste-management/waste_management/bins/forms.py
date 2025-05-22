from django import forms
from .models import WasteBin
from .utils import validate_location_with_nominatim  # Import the validation function

class WasteBinForm(forms.ModelForm):
    class Meta:
        model = WasteBin
        fields = ['identifier', 'bin_type', 'location', 'latitude', 'longitude', 'current_status']

    def clean(self):
        cleaned_data = super().clean()
        latitude = cleaned_data.get('latitude')
        longitude = cleaned_data.get('longitude')

        # Validate the location using Nominatim
        if not validate_location_with_nominatim(latitude, longitude):
            raise forms.ValidationError("The latitude and longitude do not correspond to Surigao City.")

        return cleaned_data